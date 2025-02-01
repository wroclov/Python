import requests
import grpc
import math_pb2
import math_pb2_grpc

def test_rest_api():
    response = requests.get("http://localhost:8000/calculate?operation=add&a=2&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_grpc_api():
    channel = grpc.insecure_channel("localhost:50051")
    stub = math_pb2_grpc.MathServiceStub(channel)
    response = stub.Calculate(math_pb2.MathRequest(operation="add", a=2, b=3))
    assert response.result == 5

def test_graphql_api():
    query = '{ calculate(operation: "add", a: 2, b: 3) { result } }'  # Fix: explicitly request `result`
    response = requests.post("http://localhost:8001/graphql", json={"query": query})
    assert response.status_code == 200
    assert response.json()["data"]["calculate"]["result"] == 5  # Fix: navigate to `result`
