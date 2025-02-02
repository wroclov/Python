Steps to build and run project.
rest_api
uvicorn rest_api:app --host 0.0.0.0 --port 8000

proto buf
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. math.proto

grpc_server.py 
python grpc_server.py

GraphQL_api.py
uvicorn graphql_api:app --host 0.0.0.0 --port 8001

websocket_server.py
uvicorn websocket_server:app --host 0.0.0.0 --port 8002

benchmark.py 
