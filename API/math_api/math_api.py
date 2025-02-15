from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

app = FastAPI()
security = HTTPBearer()

# Simulated authentication function
def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials.credentials != "supersecrettoken":
        raise HTTPException(status_code=403, detail="Invalid token")
    return credentials.credentials

# Request model
class MathRequest(BaseModel):
    operation: str
    a: float
    b: float

# Endpoints with security
@app.post("/calculate")
def calculate(request: MathRequest, token: str = Depends(get_current_user)):
    if request.operation == "add":
        return {"result": request.a + request.b}
    elif request.operation == "subtract":
        return {"result": request.a - request.b}
    elif request.operation == "multiply":
        return {"result": request.a * request.b}
    elif request.operation == "divide":
        if request.b == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        return {"result": request.a / request.b}
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

# Health check endpoint (no security)
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Math API! Use /docs for API exploration."}
