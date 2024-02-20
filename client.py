import socket

HOST = 'localhost'
PORT = 9090

# Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))

    while True:

        # Ends the connection
        token = socket.recv(1024).decode()
        if token == "EOF":
            print("Conversation completed")
            break

        #
        incoming = socket.recv(1024).decode()
        print("Client Robot: ", incoming)

        # Sends script
        socket.sendall("client".encode())
