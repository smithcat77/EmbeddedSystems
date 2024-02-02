```
from maestro import Controller

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
```