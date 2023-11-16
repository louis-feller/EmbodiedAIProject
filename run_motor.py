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

# Define Constants
TRAVEL_TIME = 5705
CLOSING_SPEED = -700
OPENING_SPEED = -CLOSING_SPEED

# Define Grabber class
class Grabber:
    def __init__(self, motor):
        self._motor = motor

    def down(self):
        self._motor.run_timed(time_sp=TRAVEL_TIME, speed_sp=CLOSING_SPEED)
        sleep(TRAVEL_TIME / 1000)

    def up(self):
        self._motor.run_timed(time_sp=TRAVEL_TIME, speed_sp=OPENING_SPEED)
        sleep(TRAVEL_TIME / 1000)

# Initialize Grabber
grabber = Grabber(mC)

# Behavior: Follow Line
def follow_line():
    kp = 2.1 * 100
    ki = 1 * 100
    kd = 1 * 100 *0
    Tp = -19

    black = 4
    white = 35
    offset = (black + white) / 2
    integral = 0
    derivative = 0.0
    lastError = 0

    while True:
        sleep(0.05)
        light = cs.reflected_light_intensity
        error = light - offset
        print("Error:", error)
        derivative = error - lastError
        Turn = (kp * error + ki * integral + kd * derivative) / 100
        powerLw = Tp - Turn
        powerRw = Tp + Turn
        lastError = error

        if powerLw > 100:
            powerLw = 100
        if powerRw > 100:
            powerRw = 100
        if powerLw < -100:
            powerLw = -100
        if powerRw < -100:
            powerRw = -100

        roues.on(powerLw,powerRw)
        if light > 68:
            roues.off()
            spkr.beep()
            break

        # if abs(error) > 20:
        #     search_counter += 1
        #     if search_counter <= max_search_attempts:
        #         # Perform a search behavior (e.g., turn in place)
        #         roues.on(-30, 30)  # Adjust the turn speeds as needed
        #         sleep(1)  # Adjust the search time as needed
        #     else:
        #         # If maximum search attempts reached, stop the robot or take other actions
        #         roues.off()
        #         print("Lost the line and reached maximum search attempts.")
        #         # You may add additional actions or behaviors here
        #
        #         # Reset the search counter for the next line following attempt
        #         search_counter = 0

# Behavior: Detect Can and Grab
def detect_can_and_grab():
    # Implement the logic for detecting the can and grabbing it using the grabber
    mA = Motor(OUTPUT_A)
    mD = Motor(OUTPUT_D)

    spkr.beep()

    timemin = 0
    min_distance = us.distance_centimeters  # Store the minimum distance
    time1 = 0

    # Move the robot forward and update the minimum distance
    while time1 <= 10000:
        mD.run_timed(time_sp=100, speed_sp=-100)
        sleep(0.1)
        time1 += 100
        current_distance = us.distance_centimeters
        if current_distance < min_distance:
            min_distance = current_distance
            timemin = time1

    # Move the robot backward and update the minimum distance
    mD.run_timed(time_sp=4000, speed_sp=100)
    sleep(4)
    time2 = 0
    while time2 > -10000:
        mA.run_timed(time_sp=100, speed_sp=-100)
        sleep(0.1)
        time2 -= 100
        current_distance = us.distance_centimeters
        if current_distance < min_distance:
            min_distance = current_distance
            timemin = time2

    print('Timemin :', timemin)

    # Move the robot back to the position of minimum distance
    if timemin <= 0:
        mA.run_timed(time_sp=(10000 + timemin) / 2.5, speed_sp=100)
        sleep((10 + timemin / 1000) / 2.5)
    else:
        mA.run_timed(time_sp=4000, speed_sp=100)
        sleep(4)
        mD.run_timed(time_sp=timemin / 2.63, speed_sp=-100)
        sleep(timemin / 1000)

    # Move the robot until the distance is greater than or equal to 4.5 cm
    while us.distance_centimeters >= 4.50:
        mA.run_timed(time_sp=1000, speed_sp=-200)
        mD.run_timed(time_sp=1000, speed_sp=-200)
        print("Distance : ", us.distance_centimeters)
    grabber.down()

# Main Behavior Loop
while True:
    # Run behaviors concurrently
    spkr.beep()
    follow_line()
    #detect_can_and_grab()
