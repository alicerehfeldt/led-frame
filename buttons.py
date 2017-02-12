import RPi.GPIO as GPIO
mport time


def redButton(channel):
    print "red button!"

def yellowButton(channel):
    print "yellow button!"

def blueButton(channel): 
    print "blue button!"



def buttonSetup():
    RED_BUTTON = 24
    YELLOW_BUTTON = 25
    BLUE_BUTTON = 19
    buttons = [RED_BUTTON, YELLOW_BUTTON, BLUE_BUTTON]

    GPIO.setmode(GPIO.BCM)
    for button in buttons:
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(RED_BUTTON, GPIO.RISING, callback=redButton, bouncetime=200)
    GPIO.add_event_detect(BLUE_BUTTON, GPIO.RISING, callback=blueButton, bouncetime=200)
    GPIO.add_event_detect(YELLOW_BUTTON, GPIO.RISING, callback=yellowButton, bouncetime=200)



buttonSetup()
while True:
    time.sleep(0.01)







