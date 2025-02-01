import grpc
from concurrent import futures
import math_pb2
import math_pb2_grpc

class MathService(math_pb2_grpc.MathServiceServicer):
    def Calculate(self, request, context):
        a, b, op = request.a, request.b, request.operation
        if op == "add":
            return math_pb2.MathResponse(result=a + b)
        elif op == "subtract":
            return math_pb2.MathResponse(result=a - b)
        elif op == "multiply":
            return math_pb2.MathResponse(result=a * b)
        elif op == "divide":
            return math_pb2.MathResponse(result=a / b if b != 0 else 0, error="Division by zero")
        return math_pb2.MathResponse(error="Invalid operation")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
math_pb2_grpc.add_MathServiceServicer_to_server(MathService(), server)
server.add_insecure_port("[::]:50051")
server.start()
print("gRPC server running on port 50051...")
server.wait_for_termination()
