from maestro import *
import time
import turtle

FWDREV = 0
LEFTRIGHT = 1
WAIST = 2
HEADTILT = 3
HEADTURN = 4
RIGHTSHDR = 5
RIGHTBICEP = 6
RIGHTELBOW = 7
RIGHTFOREARM = 8
RIGHTWRIST = 9
RIGHTGRIPCLOSE = 10
LEFTSHDR = 11
LEFTBICEP = 12
LEFTELBOW = 13
LEFTFOREARM = 14
LEFTWRIST = 15
LEFTGRIPCLOSE = 16


class Tango():
    def __int__(self):
        self.tango = Controller()
        self.turn = 6000

        self.tango.setTarget(HEADTURN, self.turn)
        self.tango.setRange(self, HEADTURN, self.tango.getMin(), self.tango.getMax())
        print("HeadTurn Range " + str(self.tango.getMin()) + str(self.tango.getMax()))

        self.tango.setTarget(HEADTILT, self.turn)
        self.tango.setRange(self, HEADTILT, self.tango.getMin(), self.tango.getMax())
        print("HeadTilt Range " + str(self.tango.getMin()) + str(self.tango.getMax()))

        self.tango.setTarget(RIGHTSHDR, self.turn)
        self.tango.setRange(self, RIGHTSHDR, self.tango.getMin(), self.tango.getMax())
        print("Right Shoulder Range " + str(self.tango.getMin()) + str(self.tango.getMax()))

        self.tango.setTarget(RIGHTBICEP, self.turn)
        self.tango.setRange(self, RIGHTBICEP, self.tango.getMin(), self.tango.getMax())
        print("Right Bicep Range " + str(self.tango.getMin()) + str(self.tango.getMax()))

        self.tango.setTarget(RIGHTELBOW, self.turn)
        self.tango.setRange(self, RIGHTELBOW, self.tango.getMin(), self.tango.getMax())
        print("Right Elbow Range " + str(self.tango.getMin()) + str(self.tango.getMax()))

        self.tango.setTarget(RIGHTFOREARM, self.turn)
        self.tango.setRange(self, RIGHTFOREARM, self.tango.getMin(), self.tango.getMax())
        print("Right Forearm Range " + str(self.tango.getMin()) + str(self.tango.getMax()))

        self.tango.setTarget(RIGHTWRIST, self.turn)
        self.tango.setRange(self, RIGHTWRIST, self.tango.getMin(), self.tango.getMax())
        print("Right Wrist Range " + str(self.tango.getMin()) + str(self.tango.getMax()))


window = turtle.Screen()
t = Tango()


# This method takes in a chanel and direction as arguments and then moves
# the motor of the corresponding channel in the desired direction.
def respondToKeyBoardEvent(chan, direction):
    currentPos = t.tango.getPosition(chan)
    newPos = 6000  # This is a global assignment of the newPos variable equal to the resting
    if direction.lower() in ["up", "right"]:                         # position of the motor
        newPos = currentPos + 100
    elif direction.lower() in ["down", "left"]:
        newPos = currentPos - 100
    else:
        print("Invalid move direction")
        pass
    t.tango.setTarget(chan, newPos)
    time.sleep(0.5)


def rightShoulderUp():
    respondToKeyBoardEvent(RIGHTSHDR, "up")


def rightShoulderDown():
    respondToKeyBoardEvent(RIGHTSHDR, "down")


def leftShoulderUp():
    respondToKeyBoardEvent(LEFTSHDR, "up")


def leftShoulderDown():
    respondToKeyBoardEvent(LEFTSHDR, "down")


def rightChickenWingOut():
    respondToKeyBoardEvent(RIGHTBICEP, "right")


def rightChickenWingIn():
    respondToKeyBoardEvent(RIGHTBICEP, "left")


def leftChickenWingOut():
    respondToKeyBoardEvent(LEFTBICEP, "left")


def leftChickenWingIn():
    respondToKeyBoardEvent(LEFTBICEP, "right")


def rightElbowExtend():
    respondToKeyBoardEvent(RIGHTELBOW, "down")


def rightElbowRetract():
    respondToKeyBoardEvent(RIGHTELBOW, "up")


def leftElbowExtend():
    respondToKeyBoardEvent(LEFTELBOW, "down")


def leftElbowRetract():
    respondToKeyBoardEvent(LEFTELBOW, "up")

#####
# window.onkeypress(doSomething, "someKey")
#####

window.listen()
