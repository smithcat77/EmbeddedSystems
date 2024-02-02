from maestro import *
import time
import turtle

window = turtle.Screen()


class Tango:
    def __init__(self):
        self.tango=Controller()
        self.turn = 6000
        #self.tango.setTarget(HEADTURN,self.turn)


t = Tango()

def rightShoulderUp():
    motor = 5
    turn = 8000
    t.tango.setTarget(motor,turn)


window.onkeypress(rightShoulderUp, 'r')


window.listen()
