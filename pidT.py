from ev3dev.auto import *
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, follow_for_ms
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.led import Leds
import time

mA = OUTPUT_A  # wheel
mB = Motor(OUTPUT_B)
mC = Motor(OUTPUT_C)
mD = OUTPUT_D  # wheel

ts = TouchSensor()
cs = ColorSensor()
spkr = Sound()
gs = GyroSensor()
us = UltrasonicSensor()
leds = Leds()


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)


gs.reset()
kp = 1.32 * 100
ki = 0.025 * 100
kd = 1.6 * 100 * 1
Tp = -17

offset = 19
integral = 0
derivative = 0.0
lastError = 0

roues = MoveTank(mA, mD)
count = 0

while (True):

        while gs.angle > 1000.0:
            #roues.sleep_time(0.010)
            Tp += -6





    light = cs.reflected_light_intensity
    print("Light : ", light,"\n Count : ", count,"\n Angle :",gs.angle)
    error = light - offset
    #print("Error : ", error)
    integral = integral + error
    derivative = error - lastError
    Turn = (kp * error + ki * integral + kd * derivative) / 100
    #print("Turn :", Turn)
    powerLw = Tp - Turn
    powerRw = Tp + Turn
    lastError = error
    #print("L :", powerLw, " /  R : ", powerRw)
    roues.on(clamp(powerLw, -100, 100), clamp(powerRw, -100, 100))

    # sleep(2)
