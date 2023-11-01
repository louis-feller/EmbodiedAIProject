from ev3dev.auto import *
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
import time

A = Motor(OUTPUT_A) #wheel
B = Motor(OUTPUT_B)
C = Motor(OUTPUT_C)
D = Motor(OUTPUT_D) #wheel

ts = TouchSensor()
cs = ColorSensor()
us = UltrasonicSensor()
leds = Leds()

# Motors Control
roues = MoveTank(A,D)
roues.on_for_seconds(40,40,5)

'''
while True:
    if ts.is_pressed:
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")
    else:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")
    # don't let this loop use 100% CPU
    sleep(0.010)
    m = Motor(OUTPUT_B)
    m.run_timed(time_sp=1501, speed_sp=-500) #negatif = fermeture

while not ts.is_pressed:
    #A.run_timed(speed_sp=-100)
    #D.run_timed(speed_sp=-100)
    us.MODE_US_DIST_CM
    print(us.distance_centimeters)
"""

sleep(2)
#B.run_timed(time_sp=2000,speed_sp=-500)  # negatif = fermeture
