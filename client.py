import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


# Define the server address and port
server_address = ('localhost', 12345)

# Connect the socket to the server address and port
client_socket.connect(server_address)

# Send data to the server
message = "Hello, server! This is the client."
client_socket.sendall(message.encode())

# Receive and print data from the server
data = client_socket.recv(1024)
print(f"Received: {data.decode()}")

# Close the socket
client_socket.close()