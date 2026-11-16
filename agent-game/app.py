
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

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

print("Looking for .env at:", ENV_FILE)
print(".env exists:", ENV_FILE.is_file())

load_dotenv(ENV_FILE, override=True)

print("API key loaded:", bool(os.getenv("OPENAI_API_KEY")))

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


async def main():
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is missing. Add it to your .env file."
        )

    print("1. Initializing model...", flush=True)
    model = init_chat_model("openai:gpt-6-luna")

    client = MultiServerMCPClient({
        "game": {
            "transport": "stdio",
            "command": sys.executable,
            "args": [str(BASE_DIR / "game_server.py")],
        }
    })

    print("2. Connecting to MCP server...", flush=True)

    # Keep one MCP session alive during the CLI session.
    async with client.session("game") as session:
        tools = await load_mcp_tools(session)
        print(
            "3. MCP tools loaded: " +
            ", ".join(tool.name for tool in tools),
            flush=True,
        )

        model_with_tools = model.bind_tools(tools)

        system_message = SystemMessage(content="""
You are a friendly Tic-Tac-Toe assistant.

Rules:
- Use MCP tools for all game operations.
- Never invent a board state or claim a move succeeded
  unless a tool confirms it.
- The board positions are numbered:
  0 | 1 | 2
  ---------
  3 | 4 | 5
  ---------
  6 | 7 | 8
- X moves first. O moves next.
- The user controls X. Do not make an X move on their behalf.
- If the user asks you to play as O, make a legal O move
  only when it is O's turn.
- After a game operation, show the board and explain
  whose turn it is or whether the game has ended.
- If a move fails, explain the error.
""".strip())

        def call_model(state: MessagesState):
            response = model_with_tools.invoke(state["messages"])
            return {"messages": [response]}

        builder = StateGraph(MessagesState)
        builder.add_node("model", call_model)
        builder.add_node("tools", ToolNode(tools))

        builder.add_edge(START, "model")
        builder.add_conditional_edges("model", tools_condition)
        builder.add_edge("tools", "model")

        graph = builder.compile()

        history = [system_message]

        print("\nTic-Tac-Toe assistant ready!")
        print("Try: Start a new game")
        print("Type 'quit' to exit.\n")

        while True:
            try:
                user_input = input("You: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break

            if user_input.lower() in {"quit", "exit"}:
                print("Goodbye!")
                break

            if not user_input:
                continue

            history.append(HumanMessage(content=user_input))

            try:
                result = await graph.ainvoke(
                    {"messages": history},
                    config={"recursion_limit": 15},
                )
                history = result["messages"]

                answer = history[-1].content

                if isinstance(answer, str):
                    text = answer
                elif isinstance(answer, list):
                    text = "\n".join(
                        block["text"]
                        for block in answer
                        if isinstance(block, dict)
                        and block.get("type") == "text"
                        and isinstance(block.get("text"), str)
                    )
                else:
                    text = ""

                print(f"\nAssistant: {text or '(No text response)'}\n")

            except Exception as exc:
                print(f"\nRequest failed: {exc}\n")


if __name__ == "__main__":
    asyncio.run(main())
