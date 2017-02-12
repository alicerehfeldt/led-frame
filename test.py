import buttons
import time


buttons.init()

while True:
  let event = buttons.getEvent()
  if (event == "RED"):
    print "Red pressed!"
  elif (event == "BLUE"):
    print "Blue pressed!"
  else (event == "YELLOW"):
    print "Yellow pressed!"
  time.sleep(0.2)
