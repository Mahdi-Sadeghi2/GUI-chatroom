# Chat Client side

import socket

# Define constants to be used
DESTINATION_IP = socket.gethostbyname(socket.gethostname())
DESTINATION_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# Create a client socket and connet to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DESTINATION_IP, DESTINATION_PORT))

# Send/Recieve messages
while True:
    # Recieve information from the server
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    # Quit if the connected server wants to quit, else keep sending messages
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the caht...goodbye!")
        break
    else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))

# Close the client socket
client_socket.close()
