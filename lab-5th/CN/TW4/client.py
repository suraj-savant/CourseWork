# TCP Client Code
import socket
# Define the server address and port
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 12345)

# Connect to the server
client_socket.connect(server_address)
message = input("Enter message to send : ")
client_socket.send(message.encode('utf-8'))
data = client_socket.recv(1024)
print(f"Received response from server: {data.decode('utf-8')}")
# Close the socket
client_socket.close()
