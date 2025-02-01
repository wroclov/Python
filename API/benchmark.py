import time
import requests
import grpc
import math_pb2
import math_pb2_grpc

a, b = 10, 5
operation = "multiply"

# REST Benchmark
start = time.time()
response = requests.get(f"http://localhost:8000/calculate?operation={operation}&a={a}&b={b}")
print(f"REST API Time: {time.time() - start:.4f}s, Response: {response.json()}")

# gRPC Benchmark
channel = grpc.insecure_channel("localhost:50051")
stub = math_pb2_grpc.MathServiceStub(channel)
start = time.time()
response = stub.Calculate(math_pb2.MathRequest(operation=operation, a=a, b=b))
print(f"gRPC Time: {time.time() - start:.4f}s, Response: {response.result}")

# GraphQL Benchmark (Fixed Query)
query = f'{{ calculate(operation: "{operation}", a: {a}, b: {b}) {{ result error }} }}'
start = time.time()
response = requests.post("http://localhost:8001/graphql", json={"query": query})
print(f"GraphQL Time: {time.time() - start:.4f}s, Response: {response.json()}")
