import pytest
from fastapi.testclient import TestClient
from math_api import app

client = TestClient(app)
AUTH_HEADER = {"Authorization": "Bearer supersecrettoken"}

def test_addition():
    response = client.post("/calculate", json={"operation": "add", "a": 2, "b": 3}, headers=AUTH_HEADER)
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_invalid_token():
    response = client.post("/calculate", json={"operation": "add", "a": 2, "b": 3}, headers={"Authorization": "Bearer wrongtoken"})
    assert response.status_code == 403

def test_divide_by_zero():
    response = client.post("/calculate", json={"operation": "divide", "a": 10, "b": 0}, headers=AUTH_HEADER)
    assert response.status_code == 400
    assert response.json()["detail"] == "Division by zero"

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
