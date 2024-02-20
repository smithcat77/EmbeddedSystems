import pyttsx3
import threading

class TTS(threading.Thread):

    def __int__(self):
        super(TTS, self).__init__()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)

    def run(self):
        self.engine.startLoop(False)

    def say(self, text):
        self.engine.say(text)
        # Non-blocking speaker
        self.engine.iterate()

    def stop(self):
        self.engine.endLoop()

tts = TTS()

# Starts the TTS thread
tts.start()

# Testing
tts.say("Hello, I am your robot!")

# More Testing
while True:
    text = input("Enter text to speak: ")
    tts.say(text)