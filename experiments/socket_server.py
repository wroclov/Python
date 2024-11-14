import socket

# Server setup
host = '127.0.0.1'  # Localhost
port = 8080         # Port to listen on

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the specified IP and port
server_socket.bind((host, port))
server_socket.listen(5)  # Allows up to 5 concurrent connections
print(f"Server is listening on {host}:{port}")

# Start listening for incoming connections
server_socket.listen()
print(f"Server listening on {host}:{port}")

try:
    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected by {client_address}")

        # Handle the client connection in a loop
        with client_socket:
            while True:
                # Receive data from the client
                data = client_socket.recv(1024)
                if not data:  # No data means the client has disconnected
                    print(f"Client {client_address} disconnected")
                    break
                print(f"Received from {client_address}: {data.decode()}")

                # Send a response to the client
                text_response = f"Hello, Client!, your message: {data.decode()} "
                client_socket.sendall(text_response.encode())

except KeyboardInterrupt:
    print("\nServer shutting down...")
finally:
    server_socket.close()
