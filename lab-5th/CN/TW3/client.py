import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)
while True :
    message = input('Enter a message: ')
    # Send data to the server
    client_socket.send(message.encode())
    
# Close the socket (this will never be reached in this example)
client_socket.close()

