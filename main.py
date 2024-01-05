from hue_api import hueAPI
import RPi.GPIO as GPIO
import time


hue = hueAPI()


# GPIO pin number where the sensor is connected
SENSOR_PIN = 18 

GPIO.setmode(GPIO.BCM)  # BCM pin numbering
GPIO.setup(SENSOR_PIN, GPIO.IN)  # Set the sensor pin as input

try:
    while True:
        num = GPIO.input(SENSOR_PIN)
        if num == 1:
            print('water detected')
            # use hue api to change light color to blue
            hue.changeColor(0.15, .20)
        else:
            print('no water')
            hue.changeColor(0.39, 0.33)
except KeyboardInterrupt:
    GPIO.cleanup()

