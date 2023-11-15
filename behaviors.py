from ev3dev2.motor import Motor,MoveDifferential, OUTPUT_A, OUTPUT_D, OUTPUT_C, SpeedPercent
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.wheel import Wheel
from grabber import Grabber

motors = MoveDifferential(OUTPUT_A, OUTPUT_D,wheel_class=Wheel(49.6,28),wheel_distance_mm=170)
grab_motor = Motor(OUTPUT_C)
us = UltrasonicSensor()
ts = TouchSensor()
grabber = Grabb
er(motor=grab_motor, touch_sensor=ts)

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
    mA.run_timed(time_sp=1500, speed_sp=-300)
    mD.run_timed(time_sp=1500, speed_sp=-300)
    sleep(1.5)
    timemin=0
    min=us.distance_centimeters
    time1=0
    while time1<=5000:
        mD.run_timed(time_sp=100, speed_sp=-100)
        sleep(0.1)
        time1+=100
        if us.distance_centimeters<min:
            min=us.distance_centimeters
            timemin=time1
    mD.run_timed(time_sp=5000, speed_sp=100)
    sleep(1.5)
    time2=0
    while time2>-5000:
        mA.run_timed(time_sp=100, speed_sp=-100)
        sleep(0.1)
        time2-=100
        if us.distance_centimeters<min:
            min=us.distance_centimeters
            timemin=time2
    if timemin<=0:
        mA.run_timed(time_sp=5000+timemin, speed_sp=100)
        sleep(5000+timemin)
    else:
        mA.run_timed(time_sp=5000, speed_sp=100)
        sleep(5000)
        mD.run_timed(time_sp=timemin, speed_up=-100)
        sleep(timemin)
    grab_can()
    

    
cpt1=0
l,r=line()
while(cpt1<=10 and l>r):
    l,r=line()
    cpt1=1
detect_can()

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