import RPi.GPIO as GPIO
import time


EVENT = False

def getEvent():
    last_event = EVENT
    EVENT = False
    return last_event



def redButtonPressed(channel):
    EVENT = 'RED'

def yellowButtonPressed(channel):
    EVENT = 'YELLOW'

def blueButtonPressed(channel): 
    EVENT = 'BLUE'

def init():
    RED_BUTTON = 24
    YELLOW_BUTTON = 25
    BLUE_BUTTON = 19
    buttons = [RED_BUTTON, YELLOW_BUTTON, BLUE_BUTTON]

    GPIO.setmode(GPIO.BCM)
    for button in buttons:
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(RED_BUTTON, GPIO.RISING, callback=redButtonPressed, bouncetime=200)
    GPIO.add_event_detect(BLUE_BUTTON, GPIO.RISING, callback=blueButtonPressed, bouncetime=200)
    GPIO.add_event_detect(YELLOW_BUTTON, GPIO.RISING, callback=yellowButtonPressed, bouncetime=200)
