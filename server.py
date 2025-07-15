import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)  


# Define the server address and port
server_address = ('localhost', 12345)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections (maximum of 1 connection in the queue)
server_socket.listen(1)

print(f"Server is listening on {server_address[0]}:{server_address[1]}")

# Accept incoming connection
client_socket, client_address = server_socket.accept()

# Receive and print data from the client
data = client_socket.recv(1024)
print(f"Received: {data.decode()}")

# Send a response back to the client
message = "Hello, client! This is the server."
client_socket.sendall(message.encode())

# Close the sockets
client_socket.close()
server_socket.close()