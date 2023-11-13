from threading import Thread, Event
import behaviors

follow_ev = Event
grab_ev = Event
back_ev = Event

can_grabbed = True
can_detected = True


''' Main thread :
Reads the sensor input and manages the other threads accordingly
to implement the subsumption architecture
'''
def subsume() :
    prev_dist = 0
    while() : #loop forever
        touch, distance, color = get_sensor_input()
        if abs(distance - prev_dist) > 20 :
            can_detected = True
        prev_dist = distance
        manage_event(touch, back_ev)
        manage_event(can_detected, grab_ev)
        manage_event(color, follow_ev)
        
def manage_event(f, event) :
    if f() :
        event.set()
    else :
        event.clear()

def get_sensor_input() :
    return (True, 20, 50)

sensor_input = Thread(target = subsume)
follow = Thread(target = behaviors.follow_line)
grab = Thread(target = behaviors.grab)
back = Thread(target = behaviors.go_back)
