import requests
import grpc
import json
import asyncio
import websockets
import math_pb2
import math_pb2_grpc
import pytest

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
    query = '{ calculate(operation: "add", a: 2, b: 3) { result } }'  # Explicitly request `result`
    response = requests.post("http://localhost:8001/graphql", json={"query": query})
    assert response.status_code == 200
    assert response.json()["data"]["calculate"]["result"] == 5  # Navigate to `result`

# WebSocket API Test
@pytest.mark.asyncio
async def test_websocket_api():
    uri = "ws://localhost:8002/ws"
    async with websockets.connect(uri) as websocket:
        request = json.dumps({"operation": "add", "a": 2, "b": 3})
        await websocket.send(request)
        response = await websocket.recv()
        response_data = json.loads(response)

        assert "result" in response_data
        assert response_data["result"] == 5
        assert response_data.get("error") is None  # Ensure no errors


# Run WebSocket test asynchronously as this is true nature of this API
if __name__ == "__main__":
    test_rest_api()
    test_grpc_api()
    test_graphql_api()
    asyncio.run(test_websocket_api())
