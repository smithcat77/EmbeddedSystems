import pyttsx3
from maestro import Controller
import random
import time

script = [
    "Hello there!",
    "Welcome to our demonstration.",
    "Today, we're showcasing the capabilities of our robot.",
    "This robot can perform a variety of tasks with its arms and head.",
    "For example, it can raise its right arm.",
    "Or lower its right forearm.",
    "It can also turn its head left or right.",
    "These movements are all controlled by our software.",
    "Isn't that amazing?",
    "Now, let me tell you a little more about our project.",
    "We've been working on this robot for months.",
    "It's been a challenging but rewarding journey.",
    "And we're excited to share our progress with you.",
    "In the future, we hope to integrate more advanced features.",
    "Such as facial recognition and natural language processing.",
    "Imagine a robot that can understand and respond to your commands.",
    "That's our ultimate goal.",
    "But for now, let's focus on what we've achieved so far.",
    "Our robot is a testament to the power of innovation and collaboration.",
    "Thank you for joining us today.",
    "We hope you enjoyed the demonstration.",
    "And we look forward to seeing you again soon!",
    "Goodbye for now!"
]

library = {
    'raise right arm': 'raiseRightarm',
    'lower right arm': 'lowerRightarm',
    'raise right forearm': 'raiseRightforearm',
    'lower right forearm': 'lowerRightforearm',
    'raise right bi': 'raiseRightbi',
    'lower right bi': 'lowerRightbi',
    'raise head': 'raiseHead',
    'lower head': 'lowerHead',
    'head left': 'headLeft',
    'head right': 'headRight'
}

class Robot:
    def __init__(self):
        self.control = Controller()

    def raiseRightarm(self):
        self.control.setTarget(5, 6300)
        time.sleep(0.1)

    def lowerRightarm(self):
        self.control.setTarget(5, 5900)
        time.sleep(0.1)

    def raiseRightforearm(self):
        self.control.setTarget(8, 6500)
        time.sleep(0.1)

    def lowerRightforearm(self):
        self.control.setTarget(8, 4500)
        time.sleep(0.1)

    def raiseRightbi(self):
        self.control.setTarget(6, 6500)
        time.sleep(0.1)

    def lowerRightbi(self):
        self.control.setTarget(6, 4500)
        time.sleep(0.1)

    def raiseHead(self):
        self.control.setTarget(4, 6500)
        time.sleep(0.1)

    def lowerHead(self):
        self.control.setTarget(4, 4500)
        time.sleep(0.1)

    def headLeft(self):
        self.control.setTarget(3, 7000)
        time.sleep(0.1)

    def headRight(self):
        self.control.setTarget(3, 4500)
        time.sleep(0.1)

    def gesture(self):
        movement = random.choice(list(library.keys()))
        print(f"Robot is gesturing: {movement}")
        if movement in library:
            getattr(self, library[movement])()

class TTS:
    def __init__(self, robot):
        self.robot = robot
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 125)

    def speak(self, text):
        for line in text:
            self.engine.say(line)
            self.engine.runAndWait()
            start = time.time()
            duration = 45
            while time.time() - start < duration:
                self.robot.gesture()
                time.sleep(0.5)

if __name__ == "__main__":
    robot = Robot()
    my_speech = TTS(robot)
    my_speech.speak(script)
