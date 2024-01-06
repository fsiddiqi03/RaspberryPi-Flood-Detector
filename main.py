from hue_api import hueAPI
import RPi.GPIO as GPIO
import time


def main(): 
    # create the hueAPI object 
    hue = hueAPI()


    # GPIO pin number where the sensor is connected
    SENSOR_PIN = 18 

    GPIO.setmode(GPIO.BCM)  # BCM pin numbering
    GPIO.setup(SENSOR_PIN, GPIO.IN)  # Set the sensor pin as input


    light_changed = False

    try:
        while True:
            num = GPIO.input(SENSOR_PIN)
            # 1 means water is deteced 
            if num == 1:
                print('water detected')
                if not light_changed:
                    # use hue api to change light color to blue
                    hue.changeColor(0.15, .20)
                    light_changed = True
            # checks if the GPIO sends back 0, meaning no water 
            else:
                print('no water')
                # if the light was changed, meaning its blue, return it back to its normal state 
                if light_changed:
                    hue.changeColor(0.39, 0.33)
                    light_changed = False
            time.sleep(0.25)
    except KeyboardInterrupt:
        GPIO.cleanup()



if __name__ == '__main__':
    main()