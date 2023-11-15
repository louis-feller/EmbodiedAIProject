from ev3dev.auto import *
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, follow_for_ms
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.led import Leds
from ev3dev2.button import Button
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


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)


gs.reset()
# parametres nuit :
kp = 3.3 * 100
ki = 2.0 * 100
kd = 1.9 * 100
Tp = -18

# Calibrer avant !!!
offset = 45.0
integral = 0
derivative = 0.0
lastError = 0
while True and not buttons.up:


    while gs.angle > 1000.0:
        # roues.sleep_time(0.010)
        Tp += -6
    sleep(0.002)
    light = cs.reflected_light_intensity
    error = light - offset
    print("Error : ", error)
    derivative = error - lastError
    Turn = (kp * error + ki * integral + kd * derivative) / 100
    powerLw = Tp - Turn
    powerRw = Tp + Turn
    lastError = error
    roues.on(clamp(powerLw, -100, 100), clamp(powerRw, -100, 100))

    # sleep(2)
