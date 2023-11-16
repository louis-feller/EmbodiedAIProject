#imports

from ev3dev.auto import *
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, follow_for_ms
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.led import Leds
import time

#I/O

mA = OUTPUT_A  # wheel
mB = Motor(OUTPUT_B)
mC = Motor(OUTPUT_C)
mD = OUTPUT_D  # wheel
roues = MoveTank(mA, mD)

ts = TouchSensor()
cs = ColorSensor()
spkr = Sound()
gs = GyroSensor()
us = UltrasonicSensor()

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
def move(Tp):
    kp = 3.3 * 100
    ki = 2.0 * 100
    kd = 1.9 * 100
    offset = 15

    integral = 0
    derivative = 0.0
    lastError = 0

    while True:
        light = cs.reflected_light_intensity
        error = light - offset
        print("Error : ", error)
        derivative = error - lastError
        Turn = (kp * error + ki * integral + kd * derivative) / 100
        powerLw = Tp - Turn
        powerRw = Tp + Turn
        lastError = error

        roues.on(clamp(powerLw, -100, 100), clamp(powerRw, -100, 100))

#################################

import time
import random


class DetectCanBehavior:
    def __init__(self, robot):
        self.robot = robot

    def execute(self):
        print("Detecting can...")
        # Implement can detection logic
        # For simplicity, simulate can detection with a random result
        can_detected = random.choice([True, False])

        if can_detected:
            print("Can detected!")
            self.robot.change_behavior("grab_can")
        else:
            print("No can detected.")
            self.robot.change_behavior("wander")


class GrabCanBehavior:
    def __init__(self, robot):
        self.robot = robot

    def execute(self):
        print("Grabbing can...")
        # Implement can grabbing logic
        # For simplicity, just print a message
        print("Can grabbed!")
        self.robot.change_behavior("wander")


class WanderBehavior:
    def __init__(self, robot):
        self.robot = robot

    def execute(self):
        print("Wandering...")
        # Implement wandering logic
        # For simplicity, just turn randomly

        time.sleep(2)


class Robot:
    def __init__(self):
        self.behavior = None

    def set_behavior(self, behavior):
        self.behavior = behavior

    def change_behavior(self, behavior_name):
        # Change the current behavior
        if behavior_name == "detect_can":
            self.set_behavior(DetectCanBehavior(self))
        elif behavior_name == "grab_can":
            self.set_behavior(GrabCanBehavior(self))
        elif behavior_name == "wander":
            self.set_behavior(WanderBehavior(self))
        else:
            raise ValueError(f"Unknown behavior: {behavior_name}")

    def execute_behavior(self):
        # Execute the current behavior
        if self.behavior:
            self.behavior.execute()

    def turn(self, direction):
        # Implement turn logic
        print(f"Turning {direction}")
        # Actual implementation will depend on your robot hardware


# Example of using the behavioral architecture
robot = Robot()
robot.change_behavior("detect_can")

for _ in range(5):
    robot.execute_behavior()

Kp = 0.5  # Coefficient proportionnel
Ki = 0.01  # Coefficient intégral
Kd = 0.1  # Coefficient dérivé
offset = 45  # Valeur de référence du capteur de couleur
Tp = 50  # Puissance de base des moteurs

# Initialiser les variables du correcteur PID
integral = 0  # Somme des erreurs
last_error = 0  # Erreur précédente
derivative = 0  # Variation de l'erreur


# Définir une fonction line follower qui suit le côté gauche de la ligne noire
def line_follower():
    # Boucler indéfiniment
    while True:
        # Lire la valeur du capteur de couleur
        light_value = cs.reflected_light_intensity

        # Calculer l'erreur par rapport à la valeur de référence
        error = light_value - offset

        # Calculer la somme des erreurs
        integral = integral + error

        # Calculer la variation de l'erreur
        derivative = error - last_error

        # Calculer la correction à appliquer aux moteurs
        turn = Kp * error + Ki * integral + Kd * derivative

        # Mettre à jour l'erreur précédente
        last_error = error

        # Calculer la puissance des moteurs gauche et droit
        power_left = Tp + turn
        power_right = Tp - turn

        # Ajuster la puissance des moteurs si elle dépasse les limites
        if power_left > 100:
            power_left = 100
        if power_right > 100:
            power_right = 100
        if power_left < -100:
            power_left = -100
        if power_right < -100:
            power_right = -100

        # Faire avancer le robot avec les puissances calculées
        roues.on(power_left, power_right)

        # Si le capteur de couleur détecte du blanc, arrêter le robot et faire un son
        if light_value > 80:
            roues.off()
            spkr.beep()
            break


# Appeler la fonction line follower
line_follower()



