from ev3dev2.motor import Motor,MoveDifferential, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2
from grabber import close, open

motors = MoveDifferential(OUTPUT_A, OUTPUT_B)
gripper = Motor(OUTPUT_C)
us = UltrasonicSensor()
ts = TouchSensor()

'''Can was detected
- open gripper
- run into can
- close gripper
- track backwards to line (hopefully)'''
def grab() :
    open(gripper,2000)
    distance = us.us_distance_centimeters
    motors.on_for_distance(distance_mm = distance/10)


    




