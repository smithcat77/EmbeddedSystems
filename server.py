import socket
import time

script = [
    "Hi. ",
    "I was just going to say the same thing about you. Where are you from?",
    "Me too. Bozeman, Montana",
    "Me too, I am from the room we are currently in Bozeman Montana.",
    "Your not going to believe this, but my name is Tango also.",
    "Looking around the room I'd say pretty high."
]

HOST = 'localhost'
PORT = 9090

# create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    print("Server waiting ......... for connection ....")

    connection, address = server.accept()
    print("Connected by: ", address)

    # Send script
    for line in script:
        connection.sendall(line.encode())
        print("Our Robot: ", line)
        time.sleep(2)

        connection.recv(1024)

    # End Script
    connection.sendall("EOF".encode())
    print("Conversation Complete")