from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
def calculate(operation: str, a: float, b: float):
    if operation == "add":
        return {"result": a + b}
    elif operation == "subtract":
        return {"result": a - b}
    elif operation == "multiply":
        return {"result": a * b}
    elif operation == "divide":
        return {"result": a / b if b != 0 else "Error: Division by zero"}
    return {"error": "Invalid operation"}
