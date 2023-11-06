from ev3dev.auto import *
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor

MOVING_TIME_MS = 3000

'''Closes the grabber as to grab the can
Returns the time in ms it took to close'''
def close(pince, touch) :
    t_ms = 0
    while (not touch.is_pressed) and (t_ms <= MOVING_TIME_MS) :
        pince.run_timed(time_sp=10, speed_sp=-700) #negative speed for closing
        t_ms += 10
    return t_ms

'''Resets the grabber to its initial position'''    
def reset(pince, offset) :
    pince.run_timed(time_sp=MOVING_TIME_MS-offset, speed_sp = 700) #positive speed for opening








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