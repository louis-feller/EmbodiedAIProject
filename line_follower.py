#!/usr/bin/env python3


from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, SpeedPercent, follow_for_forever
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button

from time import sleep

btn = Button() # we will use any button to stop script

tank = MoveTank(OUTPUT_A, OUTPUT_D)

# Connect an EV3 color sensor to any sensor port.

tank.cs = ColorSensor()

while not btn.any():    # exit loop when any button pressed
    tank.followline(
        kp=10, ki=0, kd=0,
        speed=SpeedPercent(30),
        follow_for=follow_for_forever
    )

    

    sleep(0.1) # wait for 0.1 seconds