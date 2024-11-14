import socket
from concurrent.futures import ThreadPoolExecutor

# Define the IP address and port of the server
host = '127.0.0.1'
port = 8080

success = 0
unsuccess = 0

# Function to handle each client request
def send_request(request_number):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global success
    global unsuccess
    try:
        s.connect((host, port))
        print(f"Connected to the server {request_number + 1}/100")

        # Send data
        text = f"Hello, Server! Request number {request_number + 1}"
        s.sendall(text.encode())

        # Receive response from the server
        data = s.recv(1024)
        print(f'Received from server ({request_number + 1}):', data.decode())
        success += 1

    except ConnectionRefusedError:
        print(f"Connection refused for request {request_number + 1}. Is the server running?")
        unsuccess += 1

    finally:
        s.close()

# Create a ThreadPoolExecutor for parallel execution
with ThreadPoolExecutor(max_workers=10000) as executor:  # Adjust max_workers as needed
    executor.map(send_request, range(20000))

print(f"Clients connections finished, successful: {success}, unsuccessful: {unsuccess}")
