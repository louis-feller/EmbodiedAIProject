from threading import Thread, Event
import grabber, follower, sensors

follow_ev = Event
grab_ev = Event
back_ev = Event

can_grabbed = True
can_detected = True

def subsume() :
    can_grabbed, can_detected = get_sensor_input()
    while() :
        manage_event(can_grabbed, back_ev)
        manage_event(can_detected, grab_ev)
        manage_event(True, follow_ev)
        
def manage_event(f, event) :
    if f() :
        event.set()
    else :
        event.clear()

def get_sensor_input() :
    return (True, True)

sensor_input = Thread(target = subsume)
follow = Thread(target = follower.follow_line)
grab = Thread(target = grabber.grab_can)
back = Thread(target = follower.go_back)
