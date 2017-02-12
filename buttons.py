import RPi.GPIO as GPIO
import time


EVENT = False

def getEvent():
    global EVENT
    last_event = EVENT
    EVENT = False
    return last_event

def redButtonPressed(channel):
    global EVENT
    print "RED BUTTON PRESSED"
    EVENT = 'RED'

def yellowButtonPressed(channel):
    global EVENT
    print "YELLOW BUTTON PRESSED"
    EVENT = 'YELLOW'

def blueButtonPressed(channel):
    global EVENT
    print "BLUE BUTTON PRESSED"
    EVENT = 'BLUE'

def init():
    RED_BUTTON = 25
    YELLOW_BUTTON = 24
    BLUE_BUTTON = 19
    buttons = [RED_BUTTON, YELLOW_BUTTON, BLUE_BUTTON]

    GPIO.setmode(GPIO.BCM)
    for button in buttons:
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(RED_BUTTON, GPIO.RISING, callback=redButtonPressed, bouncetime=200)
    GPIO.add_event_detect(BLUE_BUTTON, GPIO.RISING, callback=blueButtonPressed, bouncetime=200)
    GPIO.add_event_detect(YELLOW_BUTTON, GPIO.RISING, callback=yellowButtonPressed, bouncetime=200)
