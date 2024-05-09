from maestro import Controller
import time
import tkinter as tk
import threading
import pyttsx3

class KeyboardController:
    def __init__(self, tts):
        self.control = Controller()
        self.gear = 0
        self.left_speeds = [5200, 4500, 4000]
        self.right_speeds = [6800, 7400, 7900]
        self.tts = tts
        
        self.control.setTarget(0, 5900)
        self.control.setTarget(1, 5900)

    # Waist = 2, HeadTilt = 3, HeadPan = 4,

    # RightShldr = 5, RightBicep = 6, RightElbow = 7, RightFore = 8
    # RightWrist = 9, RightGrip = 10

    # LeftShldr = 11, LeftBicep = 12, LeftElbow = 13, LeftFore = 14,
    # LeftWrist = 15, LeftGrip = 16, empty = 17, empty = 18
    def reset(self):
        for i in range(2, 17):
            self.control.setTarget(i, 6000)
            print(i, " Iterating through the servos")

    def shiftUp(self, event):
        if self.gear < 2:
            self.gear += 1
            self.control.setTarget(0, self.left_speeds[self.gear])
            self.control.setTarget(1, self.right_speeds[self.gear])

    def shiftDown(self, event):
        if self.gear > 0:
            self.gear -= 1
            self.control.setTarget(0, self.left_speeds[self.gear])
            self.control.setTarget(1, self.right_speeds[self.gear])

    def forward(self, event):
        self.control.setTarget(0, 5200)
        self.control.setTarget(1, 6800)
        time.sleep(0.5)

    def reverse(self, event):
        self.control.setTarget(0, 6800)
        self.control.setTarget(1, 5200)
        time.sleep(0.5)

    def left(self, event):
        self.control.setTarget(1, 7000)
        time.sleep(0.5)

    def right(self, event):
        self.control.setTarget(0, 4900)

    def stop(self, event):
        if self.gear > 1:
            left_speed = 4000
            right_speed = 7900
            for _ in range(6):
                left_speed += 200
                right_speed -= 183
                self.control.setTarget(0, left_speed)
                self.control.setTarget(1, right_speed)
                time.sleep(0.5)
            self.control.setTarget(0, 5900)
            self.control.setTarget(1, 5900)
        else:
            self.control.setTarget(0, 5900)
            self.control.setTarget(1, 5900)

        def listen():
            while True:
                text = input("Enter: ").strip()
                if text.lower() == 'quit':
                    break
                if text:
                    self.tts.speak(text)

        input_thread = threading.Thread(target=listen, daemon=True)
        input_thread.start()

    def leftArm(self, event):
        for i in range(11, 15):
            self.control.setTarget(i, 5500)
            print("Moving left arm")
            time.sleep(1)
            self.control.setTarget(i, 6000)
        time.sleep(0.7)

    def rightArm(self, event):
        for i in range(5, 9):
            self.control.setTarget(i, 5500)
            print("Moving right arm")
            self.control.setTarget(i, 6000)
        time.sleep(0.7)

    def headPan(self, event):
        self.control.setTarget(4, 5900)
        time.sleep(0.7)
        self.control.setTarget(4, 4500)
        time.sleep(0.7)
        self.control.setTarget(4, 5900)
        time.sleep(0.7)
        self.control.setTarget(4, 7000)
        time.sleep(0.7)
        self.control.setTarget(4, 5900)

    def headTilt(self, event):
        self.control.setTarget(3, 5900)
        time.sleep(0.7)
        self.control.setTarget(3, 4500)
        time.sleep(0.7)
        self.control.setTarget(3, 5900)
        time.sleep(0.7)
        self.control.setTarget(3, 7000)
        time.sleep(0.7)
        self.control.setTarget(3, 5900)

    def waist(self, event):
        self.control.setTarget(2, 5900)
        time.sleep(0.7)
        self.control.setTarget(2, 3500)
        time.sleep(0.7)
        self.control.setTarget(2, 5900)
        time.sleep(0.7)
        self.control.setTarget(2, 8000)
        time.sleep(0.7)
        self.control.setTarget(2, 5900)

    def leftWrist(self, event):
        self.control.setTarget(15, 5900)
        time.sleep(0.7)
        self.control.setTarget(15, 4500)
        time.sleep(0.7)
        self.control.setTarget(15, 5900)
        time.sleep(0.7)

    def rightWrist(self, event):
        self.control.setTarget(9, 5900)
        time.sleep(0.7)
        self.control.setTarget(9, 4500)
        time.sleep(0.7)
        self.control.setTarget(9, 5900)
        time.sleep(0.7)

    def leftGrip(self, event):
        self.control.setTarget(16, 5900)
        time.sleep(0.7)
        self.control.setTarget(16, 1000)
        time.sleep(0.7)
        self.control.setTarget(16, 5900)
        time.sleep(0.7)

    def rightGrip(self, event):
        self.control.setTarget(10, 4000)
        time.sleep(0.7)
        self.control.setTarget(10, 6800)
        time.sleep(0.7)
        self.control.setTarget(10, 4000)
        time.sleep(0.7)

    def setup_keyboard_bindings(self, root):
        root.bind('<Up>', self.forward)
        root.bind('<Down>', self.reverse)
        root.bind('<Left>', self.left)
        root.bind('<Right>', self.right)
        root.bind('<space>', self.stop)
        root.bind('<w>', self.waist)
        root.bind('<h>', self.headPan)
        root.bind('<g>', self.headTilt)
        root.bind('<r>', self.rightGrip)
        root.bind('<e>', self.rightWrist)
        root.bind('<l>', self.leftGrip)
        root.bind('<i>', self.leftWrist)
        root.bind('<q>', self.reset)
        root.bind('<Shift_L>', self.shiftUp)
        root.bind('<Shift_R>', self.shiftDown)
        root.bind('<Escape>', lambda e: root.destroy())

    def start(self):
        root = tk.Tk()
        self.setup_keyboard_bindings(root)
        root.mainloop()

class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Adjust the speaking rate as needed

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

def main():
    tts = TTS()
    kb = KeyboardController(tts)
    kb.start()

if __name__ == "__main__":
    main()
