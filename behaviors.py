from ev3dev2.motor import Motor,MoveDifferential, OUTPUT_A, OUTPUT_D, OUTPUT_C, SpeedPercent
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.wheel import Wheel
from grabber import Grabber

motors = MoveDifferential(OUTPUT_A, OUTPUT_D,wheel_class=Wheel(49.6,28),wheel_distance_mm=170)
grab_motor = Motor(OUTPUT_C)
us = UltrasonicSensor()
ts = TouchSensor()
grabber = Grabber(motor=grab_motor, touch_sensor=ts)

'''Can detected :
- open gripper
- run into can
- close gripper
- track backwards to line (hopefully)'''
def grab_can() :
    sp = SpeedPercent(20)
    grabber.open()
    distance = us.us_distance_centimeters
    motors.on_for_distance(distance_mm = distance/10,speed=sp)
    grabber.close()
    motors.on_for_distance(distance_mm= -(distance/10),speed=sp)

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