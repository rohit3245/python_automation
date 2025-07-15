import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket 
server_address = ('localhost', 12345)
server_socket.bind(server_address)

#listen and accept connections 
server_socket.listen(5)
client_socket, client_address = server_socket.accept()

#connect to server
client_socket.connect(server_address)

#send and receive data 
client_socket.send(data.encode())
received_data = client_socket.recv(1024)

#close a socket 
client_socket.close()


