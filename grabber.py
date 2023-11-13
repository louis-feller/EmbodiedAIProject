from ev3dev.auto import *
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor

MAX_CLOSE = -3000
MAX_OPEN = 3000
CLOSING_SPEED = -700
OPENING_SPEED = -CLOSING_SPEED

class Grabber :
    def __init__(self, motor, touch_sensor) -> None:
        self._pos = 0
        self._motor = motor
        self._touch = touch_sensor
        
    '''Closes the grabber as to grab the can
    Returns the time in ms it took to close'''
    def close(self) :
        while (not self._touch.is_pressed) and (self._pos >= MAX_CLOSE) :
            self._otor.run_timed(time_sp=10, speed_sp=CLOSING_SPEED) #negative speed for closing
            self._pos -= 10
        self._motor.run_timed(time_sp= 280, speed_sp= CLOSING_SPEED)

    '''Open the grabber for t_ms milliseconds'''    
    def open(self) :
        self._motor.run_timed(time_sp=MAX_OPEN - self._pos, speed_sp = OPENING_SPEED) #positive speed for opening
        self._pos = MAX_OPEN

    def reset(self) :
        if self._pos > 0 : #grabber in rather open pos
            sp = CLOSING_SPEED
        else :
            sp = OPENING_SPEED
        self._motor.run_timed(time_sp=abs(self._pos), speed_sp = sp)