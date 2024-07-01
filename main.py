from email_sender import ses
import RPi.GPIO as GPIO
import time


def main(): 
    
    # create the ses object
    email = ses()

    # GPIO pin number where the sensor is connected
    SENSOR_PIN = 18 

    GPIO.setmode(GPIO.BCM)  # BCM pin numbering
    GPIO.setup(SENSOR_PIN, GPIO.IN)  # Set the sensor pin as input


    email_sent = False

    try:
        while True:
            num = GPIO.input(SENSOR_PIN)
            # 1 means water is deteced 
            if num == 1:
                print('water detected')
                if not email_sent: # only send email once. 
                    # send email
                    email.send(0)
                    email_sent = True
                    

            # checks if the GPIO sends back 0, meaning no water 
            else:
                print('no water')
                # if email was already sent, send another notifying user water is no longer detected. 
                if email_sent:
                    email.send(1)
                    email_sent = False
            time.sleep(0.25)
    except KeyboardInterrupt:
        GPIO.cleanup()



if __name__ == '__main__':
    main()
