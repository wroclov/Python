import time
import requests
import grpc
import math_pb2
import math_pb2_grpc
import matplotlib.pyplot as plt
import psutil
import os
import numpy as np

a, b = 10, 5
operation = "multiply"
num_requests = 5

# Function to measure memory usage
def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Convert to MB

# REST Benchmark
rest_times = []
start_mem = get_memory_usage()
start = time.time()
for _ in range(num_requests):
    req_start = time.time()
    response = requests.get(f"http://localhost:8000/calculate?operation={operation}&a={a}&b={b}")
    rest_times.append(time.time() - req_start)
rest_total_time = time.time() - start
rest_mem_usage = get_memory_usage() - start_mem

# gRPC Benchmark
channel = grpc.insecure_channel("localhost:50051")
stub = math_pb2_grpc.MathServiceStub(channel)
grpc_times = []
start_mem = get_memory_usage()
start = time.time()
for _ in range(num_requests):
    req_start = time.time()
    response = stub.Calculate(math_pb2.MathRequest(operation=operation, a=a, b=b))
    grpc_times.append(time.time() - req_start)
grpc_total_time = time.time() - start
grpc_mem_usage = get_memory_usage() - start_mem

# GraphQL Benchmark
query = f'{{ calculate(operation: "{operation}", a: {a}, b: {b}) {{ result error }} }}'
graphql_times = []
start_mem = get_memory_usage()
start = time.time()
for _ in range(num_requests):
    req_start = time.time()
    response = requests.post("http://localhost:8001/graphql", json={"query": query})
    graphql_times.append(time.time() - req_start)
graphql_total_time = time.time() - start
graphql_mem_usage = get_memory_usage() - start_mem

# Compute Metrics (Avoid empty lists)
rest_avg_time = np.mean(rest_times) if rest_times else 0
grpc_avg_time = np.mean(grpc_times) if grpc_times else 0
graphql_avg_time = np.mean(graphql_times) if graphql_times else 0

rest_throughput = num_requests / rest_total_time if rest_total_time > 0 else 0
grpc_throughput = num_requests / grpc_total_time if grpc_total_time > 0 else 0
graphql_throughput = num_requests / graphql_total_time if graphql_total_time > 0 else 0

# Debugging logs
print(f"REST Avg Time: {rest_avg_time:.6f}s | Throughput: {rest_throughput:.2f} req/s")
print(f"gRPC Avg Time: {grpc_avg_time:.6f}s | Throughput: {grpc_throughput:.2f} req/s")
print(f"GraphQL Avg Time: {graphql_avg_time:.6f}s | Throughput: {graphql_throughput:.2f} req/s")

print(f"REST Memory Usage: {rest_mem_usage:.2f} MB")
print(f"gRPC Memory Usage: {grpc_mem_usage:.2f} MB")
print(f"GraphQL Memory Usage: {graphql_mem_usage:.2f} MB")

# Plot Results
labels = ["REST", "gRPC", "GraphQL"]
avg_times = [rest_avg_time, grpc_avg_time, graphql_avg_time]
throughput = [rest_throughput, grpc_throughput, graphql_throughput]
memory_usage = [rest_mem_usage, grpc_mem_usage, graphql_mem_usage]

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Fix scaling by using log scale if necessary
ax[0].bar(labels, avg_times, color=['blue', 'green', 'red'])
ax[0].set_title("Average Response Time (s)")
ax[0].set_ylabel("Seconds")

ax[1].bar(labels, throughput, color=['blue', 'green', 'red'])
ax[1].set_title("Throughput (Requests/sec)")
ax[1].set_ylabel("Requests per second")
ax[1].set_yscale("log")  # Log scale to make small differences visible

ax[2].bar(labels, memory_usage, color=['blue', 'green', 'red'])
ax[2].set_title("Memory Usage (MB)")
ax[2].set_ylabel("Memory (MB)")

plt.tight_layout()
plt.show()
