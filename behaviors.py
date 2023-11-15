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

'''Can detected :
- open gripper
- run into can
- close gripper
- track backwards to line (hopefully)'''
def line():
    gs.reset()
    # parametres nuit :
    kp = 3.3 * 100
    ki = 2.0 * 100
    kd = 1.9 * 100
    Tp = -20

    # Calibrer avant !!!
    offset = 12.0
    integral = 0
    derivative = 0.0
    lastError = 0

    roues = MoveTank(mA, mD)


    while (True):
        while gs.angle > 1000.0:
            # roues.sleep_time(0.010)
            Tp += -6
        i=0
        while i<3:
            i+=1
        light = cs.reflected_light_intensity
        error = light - offset
        print("Error : ", error)
        derivative = error - lastError
        Turn = (kp * error + ki * integral + kd * derivative) / 100
        # print("Turn :", Turn)
        powerLw = Tp - Turn
        powerRw = Tp + Turn
        lastError = error
        # print("L :", powerLw, " /  R : ", powerRw)
        roues.on(clamp(powerLw, -100, 100), clamp(powerRw, -100, 100))
        return (powerLw,powerRw)
        # sleep(2)


def detect_can():
    #cpt2=0
    #roues.on(clamp(-powerLw, -100, 100), clamp(-powerRw, -100, 100))
    #while(cpt2<=10):
        #roues.on(clamp(-powerLw, -100, 100), clamp(-powerRw, -100, 100))
        #cpt2=1
    mA=Motor(OUTPUT_A)
    mD=Motor(OUTPUT_D)
    mA.run_timed(time_sp=1200, speed_sp=-300)
    mD.run_timed(time_sp=1200, speed_sp=-300)
    sleep(1.5)
    timemin=0
    min=us.distance_centimeters
    time1=0
    while time1<=10000:
        mD.run_timed(time_sp=100, speed_sp=-100)
        sleep(0.1)
        time1+=100
        if us.distance_centimeters<min:
            min=us.distance_centimeters
            timemin=time1
    mD.run_timed(time_sp=10000, speed_sp=100)
    sleep(10)
    time2=0
    while time2>-10000:
        mA.run_timed(time_sp=100, speed_sp=-100)
        sleep(0.1)
        time2-=100
        if us.distance_centimeters<min:
            min=us.distance_centimeters
            timemin=time2
    if timemin<=0:
        mA.run_timed(time_sp=10000+timemin, speed_sp=100)
        sleep(10+timemin/1000)
    else:
        mA.run_timed(time_sp=10000, speed_sp=100)
        sleep(10)
        mD.run_timed(time_sp=timemin, speed_sp=-100)
        sleep(timemin/1000)
    while us.distance_centimeters>3.5:
        mA.run_timed(time_sp=1000, speed_sp=-200)
        mD.run_timed(time_sp=1000, speed_sp=-200)
 
#cpt1=0
#l,r=line()
# while(cpt1<=10 and l>r):
#     l,r=line()
#     cpt1=1
detect_can()

grabber.open()
grabber.close()



'''No line detected :
Go at low speed in a right turn spiral forever'''
def look_for_line() :
    t = 1
    sp = SpeedPercent(20)
    while() : #loop forever
        motors.on_for_seconds(t)
        motors.turn_right(speed = sp, degrees=90)
        t += 1

def follow_line() :
    pass