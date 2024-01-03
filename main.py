import RPi.GPIO as GPIO
# import time

# GPIO pin number where the sensor is connected
SENSOR_PIN = 18 

GPIO.setmode(GPIO.BCM)  # BCM pin numbering
GPIO.setup(SENSOR_PIN, GPIO.IN)  # Set the sensor pin as input

try:
    while True:
        num = GPIO.input(SENSOR_PIN)
        if num == 1:
            print('water detected')
        else:
            print('no water')
except KeyboardInterrupt:
    GPIO.cleanup()
