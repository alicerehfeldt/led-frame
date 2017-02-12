import buttons
import os
import pprint
import pygame
import random
import subprocess
import sys
import time
import glob
pp = pprint.PrettyPrinter()

class BlackScreenException(Exception):
  pass

def initPygame():
  pygame.display.init();


def blackScreen():
  initPygame()

  black = 0, 0, 0

  screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
  screen.fill(black)
  pygame.mouse.set_visible(0)
  return screen

def pinkBox(screen):
  pink = 255, 0, 255
  pygame.draw.rect(screen, pink, (160, 120, 320, 240))
  pygame.display.update();

def stopMovie(child):
  child.stdin.write("q")


def playMovie(movie):
  print('Playing ' + movie)
  try:
    child = subprocess.Popen(['/usr/bin/omxplayer', '-n -1', '--no-osd', movie], stdin = subprocess.PIPE)
    while child.poll() is None:
      # Keyboard Events
      # ESC = quit
      # SPACE = skip
      for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
          raise BlackScreenException()
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
          stopMovie(child)
          return True

      # Button Events
      event = buttons.getEvent()
      # RED = black screen
      if (event == "RED"):
        raise BlackScreenException()
      # BLUE = mode skip
      elif (event == "BLUE"):
        stopMovie(child)
        return False
      # YELLOW = movie skip
      elif (event == "YELLOW"):
        stopMovie(child)
        return True
      time.sleep(0.1)
    return True
  except BlackScreenException:
    stopMovie(child)
    raise BlackScreenException
  except subprocess.CalledProcessError, e:
    print "omxplayer output:", e.output
    return False

def playMovies(movies):
  for movie in movies:
    playNext = playMovie(movie)
    if not playNext:
      return False
    time.sleep(2)
  return True

def sequentialPlay(path):
  movies = glob.glob(path)
  movies.sort()
  while True:
    keepPlaying = playMovies(movies)
    if not keepPlaying:
      return

def randomPlay(path):
  movies = glob.glob(path)
  while True:
    random.shuffle(movies)
    keepPlaying = playMovies(movies)
    if not keepPlaying:
      return

def done():
  pygame.display.quit()
  pygame.quit()
  sys.exit(0)


def sailorMoonClips():
  path = '/home/pi/sm/*.mp4'
  randomPlay(path)

def sailorMoonEpisodes():
  path = '/home/pi/episodes/*.mp4'
  sequentialPlay(path)

def playEverything():
  try:
    while True:
      sailorMoonClips()
      sailorMoonEpisodes()
  except BlackScreenException:
    return

def sleepMode():
  blackScreen()
  while True:
    time.sleep(0.1)
    # Button Events
    event = buttons.getEvent()
    # RED = black screen
    if (event == "RED"):
        return

try:
  buttons.init()
  screen = blackScreen()
  while True:
    playEverything()
    sleepMode()
except KeyboardInterrupt:
  print "ctrl+c"
  done()
except SystemExit:
  done()
