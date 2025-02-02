import json
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            request = json.loads(data)

            a, b, op = request["a"], request["b"], request["operation"]
            result = None
            error = None

            if op == "add":
                result = a + b
            elif op == "subtract":
                result = a - b
            elif op == "multiply":
                result = a * b
            elif op == "divide":
                result = a / b if b != 0 else 0
                error = "Division by zero" if b == 0 else None
            else:
                error = "Invalid operation"

            response = {"result": result, "error": error}
            await websocket.send_text(json.dumps(response))

        except Exception as e:
            await websocket.send_text(json.dumps({"error": str(e)}))
