from ev3dev2.motor import Motor,MoveDifferential, OUTPUT_A, OUTPUT_D, OUTPUT_C, SpeedPercent
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.wheel import Wheel
from grabber import Grabber

motors = MoveDifferential(OUTPUT_A, OUTPUT_D,wheel_class=Wheel(49.6,28),wheel_distance_mm=170)
grab_motor = Motor(OUTPUT_C)
us = UltrasonicSensor()
ts = TouchSensor()
grabber = Grabber(motor=grab_motor, touch_sensor=ts)

grabber.open()
grabber.close()
grabber.reset()

