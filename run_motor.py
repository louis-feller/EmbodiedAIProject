from ev3dev.auto import *
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, follow_for_ms
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.led import Leds
from ev3dev2.button import Button
from grabber import Grabber
import time

mA = OUTPUT_A  # wheel
mB = Motor(OUTPUT_B)
mC = Motor(OUTPUT_C)
mD = OUTPUT_D  # wheel
roues = MoveTank(mA, mD)

#ts = TouchSensor()
cs = ColorSensor()
spkr = Sound()
gs = GyroSensor()
us = UltrasonicSensor()
leds = Leds()
buttons = Button()


grabber = Grabber(mC)
grabber.down()
spkr.beep()