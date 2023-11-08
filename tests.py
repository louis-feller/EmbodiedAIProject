from ev3dev.auto import *
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B,OUTPUT_C,OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
import time

mA = OUTPUT_A #left wheel
mB = Motor(OUTPUT_B)
mC = Motor(OUTPUT_C)
mD = OUTPUT_D  #right wheel

ts = TouchSensor()
ls = LightSensor()
cs = ColorSensor()
us = UltrasonicSensor()
leds = Leds()

# Motors Control
roues = MoveTank(mA,mD)
#roues.on_for_seconds(-100,-100,3.5)


#Test light/Color sensor
while(False):
    print(ls.ambient_light_intensity)
#test grap
# mC.on_for_seconds(SpeedPercent(-40),3)
''''
3sec pour ouvrir et fermer
'''
#mC.run_timed(time_sp=3000, speed_sp=700)
def close(pince, touch) :
    MOVING_TIME_MS = 3000
    t_ms = 280
    while (not touch.is_pressed) and (t_ms < MOVING_TIME_MS) :
        pince.run_timed(time_sp=10, speed_sp=-700) #negative speed for closing
        t_ms += 10
    pince.run_timed(time_sp=280, speed_sp=-700)  # negative speed for closing
    return t_ms
def reset(pince, offset) :
    MOVING_TIME_MS = 3000
    pince.run_timed(time_sp=offset, speed_sp = 700) #positive speed for opening

x = close(mC,ts)
print(x)
#sleep(5)
#reset(mC,x)

# Ultrasonic sensor
#while(True):
#    print(us.distance_centimeters)




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
    m.run_timed(time_sp=1501, speed_sp=-500) #negatif = fermetures

while not ts.is_pressed:
    #A.run_timed(speed_sp=-100)
    #D.run_timed(speed_sp=-100)
    us.MODE_US_DIST_CM
    print(us.distance_centimeters)
'''

sleep(2)
#B.run_timed(time_sp=2000,speed_sp=-500)  # negatif = fermeture
