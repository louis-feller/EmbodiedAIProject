from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, SpeedPercent


t = 1
mt = MoveTank(OUTPUT_A, OUTPUT_B)

'''Go at low speed in a right turn spiral forever'''
def look_for_line() :
    while() : #loop forever
        mt.on_for_seconds(t)
        mt.turn_right(speed =  SpeedPercent(20), degrees=90)
        t += 1