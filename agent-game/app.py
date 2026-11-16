
import asyncio
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

# Load environment variables without overwriting existing
# environment variables.
load_dotenv(ENV_FILE)

SERVER_FILE = BASE_DIR / "game_server.py"

# Set OPENAI_MODEL in .env to a model identifier supported
# by your installed LangChain OpenAI integration.
#MODEL_NAME = os.getenv("OPENAI_MODEL")
MODEL_NAME = "openai:gpt-6-luna"

# ---------------------------------------------------------
# Agent instructions
# ---------------------------------------------------------

SYSTEM_PROMPT = """
You are a friendly and helpful Tic-Tac-Toe AI assistant.

Your role is to play Tic-Tac-Toe with the user.

Game rules:
- Always use MCP tools for game operations.
- Never invent a board state or game result.
- Only report a successful operation after receiving
  confirmation from the MCP tool.
- The board positions are numbered as follows:

    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8

- X moves first, followed by O.
- The user controls X. Never make an X move on behalf
  of the user.
- You control O.
- Only make an O move when it is O's turn.
- Always make legal moves.
- After a game operation, display the updated board
  and explain whose turn it is.
- If the game has ended, clearly announce the winner
  or draw.
- If a tool operation fails, explain the error.
- If the user asks about the current board, retrieve
  the actual game state using the appropriate MCP tool.

Keep your responses friendly and concise.
"""


# ---------------------------------------------------------
# Utility functions
# ---------------------------------------------------------

def validate_configuration():
    """Check that the required configuration is available."""

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is missing. "
            "Please add it to your .env file."
        )

    if not SERVER_FILE.is_file():
        raise FileNotFoundError(
            f"MCP server file not found: {SERVER_FILE}"
        )


def extract_response_text(content):
    """
    Extract readable text from an LLM response.

    LangChain responses can contain either a plain string
    or a list of content blocks.
    """

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_blocks = []

        for block in content:
            if isinstance(block, dict):
                if block.get("type") in {"text", "output_text"}:
                    text = block.get("text")

                    if isinstance(text, str):
                        text_blocks.append(text)

        return "\n".join(text_blocks)

    return ""


# ---------------------------------------------------------
# LangGraph agent
# ---------------------------------------------------------

def build_agent_graph(model, tools):
    """
    Build the agent workflow.

    Workflow:
        START -> model -> tools (if required) -> model
        START -> model -> END (if no tool is required)
    """

    # Allow the LLM to decide when to call MCP tools.
    model_with_tools = model.bind_tools(tools)

    async def call_model(state: MessagesState):
        """
        Invoke the LLM asynchronously using the conversation
        history provided by LangGraph.
        """

        response = await model_with_tools.ainvoke(
            state["messages"]
        )

        return {"messages": [response]}

    # Create the LangGraph state machine.
    builder = StateGraph(MessagesState)

    builder.add_node("model", call_model)
    builder.add_node("tools", ToolNode(tools))

    # Start by invoking the LLM.
    builder.add_edge(START, "model")

    # Decide whether to execute tools or finish the turn.
    builder.add_conditional_edges(
        "model",
        tools_condition
    )

    # After tool execution, return to the LLM.
    builder.add_edge("tools", "model")

    return builder.compile()


# ---------------------------------------------------------
# Main application
# ---------------------------------------------------------

async def main():

    validate_configuration()

    print("\nInitializing Tic-Tac-Toe AI agent...", flush=True)

    # Initialize the chat model.
    model = init_chat_model(MODEL_NAME)

    # Configure the external MCP server.
    client = MultiServerMCPClient({
        "game": {
            "transport": "stdio",
            "command": sys.executable,
            "args": [str(SERVER_FILE)],
        }
    })

    print("Connecting to MCP server...", flush=True)

    # Maintain an MCP session while the application runs.
    async with client.session("game") as session:

        # Discover tools exposed by the MCP server.
        tools = await load_mcp_tools(session)

        if not tools:
            raise RuntimeError(
                "No MCP tools were discovered."
            )

        print(
            "Available MCP tools:",
            ", ".join(tool.name for tool in tools),
            flush=True,
        )

        # Build the LangGraph agent.
        graph = build_agent_graph(model, tools)

        # Initialize conversation history.
        history = [
            SystemMessage(content=SYSTEM_PROMPT)
        ]

        print("\n" + "=" * 45)
        print("       TIC-TAC-TOE AI ASSISTANT")
        print("=" * 45)
        print("You play as X. The AI plays as O.")
        print("Try: Start a new game")
        print("Type 'quit' to exit.")
        print("=" * 45 + "\n")

        while True:

            try:
                user_input = input("You: ").strip()

            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break

            # Exit the application.
            if user_input.lower() in {"quit", "exit"}:
                print("Goodbye!")
                break

            if not user_input:
                continue

            # Create a new turn without modifying the
            # committed conversation history yet.
            turn_history = history + [
                HumanMessage(content=user_input)
            ]

            try:
                # Execute the LangGraph workflow.
                result = await graph.ainvoke(
                    {"messages": turn_history},
                    config={
                        "recursion_limit": 15
                    },
                )

                # Update conversation history only after
                # successful graph execution.
                history = result["messages"]

                # Extract the final assistant response.
                answer = history[-1].content
                response_text = extract_response_text(answer)

                print(
                    f"\nAssistant: {response_text or '(No text response)'}\n"
                )

            except Exception as exc:
                print(f"\nRequest failed: {exc}\n")


# ---------------------------------------------------------
# Application entry point
# ---------------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())
