import buttons
import time


buttons.init()

while True:
  event = buttons.getEvent()
  if (event == "RED"):
    print "Red pressed!"
  elif (event == "BLUE"):
    print "Blue pressed!"
  elif (event == "YELLOW"):
    print "Yellow pressed!"
  time.sleep(0.2)
