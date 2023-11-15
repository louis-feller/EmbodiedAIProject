from ev3dev.auto import *
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor

TRAVEL_TIME = 5000
CLOSING_SPEED = -700
OPENING_SPEED = -CLOSING_SPEED

class Grabber :
    def __init__(self, motor) -> None:
        self._motor = motor
        
    '''Closes the grabber'''
    def close(self) :
            self._motor.run_timed(time_sp=TRAVEL_TIME, speed_sp=CLOSING_SPEED) #negative speed for closing
            

    '''Open the grabber'''    
    def open(self) :
        self._motor.run_timed(time_sp=TRAVEL_TIME, speed_sp = OPENING_SPEED) #positive speed for opening