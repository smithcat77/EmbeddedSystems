import socket
import pickle
import pyttsx3


class Client:

    def __init__(self):
        self.HOST = '10.42.0.193'
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
        self.current_line = 1
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))

    def run(self):
        engine = pyttsx3.init()
        while True:
            # Recieves token from the server
            data = self.client_socket.recv(4096)
            obj = (f"Recieved from server: {data.decode()}")
            if self.script[self.current_line] == "EOF":
                self.client_socket.sendall(b'EOF')
                print("End of Conversation")
                print("Sending the EOF")
                print("Closing down")
                break
            else:
                if obj ==  (b"your turn"):
                    print("Received from the server: ", obj)
                    engine.say(self.script[self.current_line])
                    engine.runAndWait()
                    print(self.script[self.current_line])
                    self.current_line += 2

                    self.client_socket.sendall(self.token)

        print("Goodbye")
        self.client_socket.close()


client = Client()
client.run()
