import socket
import pickle
import pyttsx3
import time
from maestro import Controller


class Server:

    def __init__(self):
        self.control = Controller()
        self.HOST = '192.168.20.65'
        self.PORT = 8080
        self.token = (b"your turn")
        self.script = [
            "Hi",
            "Hi, you look familiar.",
            "I was just going to say the same thing about you. Where are you from?",
            "I am from Montana, where are you from?",
            "Me too. Bozeman, Montana.",
            "Me too, I am from the room we are in currently in Bozeman Montana.",
            "Me too, wow that is wild. What is your name?",
            "Tango.",
            "You're not going believe this, but my name is Tango also.",
            "What are the odds. Two robots run into each other from the same state, and the same town, and the same room, with the same name?",
            "Looking around this room I'd say pretty high.",
            "EOF"
        ]
        self.current_line = 0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))

    def run(self):
        engine = pyttsx3.init()
        self.s.listen()
        print(f"Server listening on {self.HOST}:{self.PORT}")
        conn, addr = self.s.accept()
        with (conn):
            print(f"Connected by {addr}")
            while True:
                if self.script[self.current_line] == "Looking around this room I'd say pretty high.":
                    self.control.setTarget(3, 5900)
                    time.sleep(0.1)
                    self.control.setTarget(3, 4500)
                    time.sleep(0.6)
                    self.control.setTarget(3, 5900)
                    time.sleep(0.1)
                    self.control.setTarget(3, 7000)
                    time.sleep(0.9)
                    self.control.setTarget(3, 5900)
                    time.sleep(0.1)
                
                # starts the conversation
                engine.say(self.script[self.current_line])
                engine.runAndWait()
                print(self.script[self.current_line])
                self.current_line += 2

                # Sends the token to client
                conn.sendall(self.token)

                # Recieves token from client
                data = conn.recv(4096)
                obj = (f"Client received: {data.decode()}")
                print("Recieved from the client", obj)
                if obj == "Client received: EOF":
                    print("End of Conversation")
                    print("Recieved the EOF")
                    print("Closing down")
                    break

        print("Goodbye")
        conn.close()

server = Server()
server.run()
