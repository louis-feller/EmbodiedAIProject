from ev3dev.auto import *
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, follow_for_ms
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.led import Leds
from ev3dev2.button import Button
from grabber import Grabber
import time

mA = OUTPUT_A  # wheel
mB = Motor(OUTPUT_B)
mC = Motor(OUTPUT_C)
mD = OUTPUT_D  # wheel
roues = MoveTank(mA, mD)

# ts = TouchSensor()
cs = ColorSensor()
spkr = Sound()
gs = GyroSensor()
us = UltrasonicSensor()
leds = Leds()
buttons = Button()
grabber = Grabber(mC)
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
        tank.on(power_left, power_right)

        # Si le capteur de couleur détecte du blanc, arrêter le robot et faire un son
        if light_value > 80:
            tank.off()
            sound.beep()
            break


# Appeler la fonction line follower
line_follower()