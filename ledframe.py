import os
import pprint
import pygame
import random
import subprocess
import sys
import time
import glob
pp = pprint.PrettyPrinter()

class MovieSkipException(Exception):
    pass

class MovieStopException(Exception):
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
            for event in pygame.event.get():
                if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                    raise MovieStopException()
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    raise MovieSkipException()
            time.sleep(0.1)
        return
    except MovieSkipException:
        stopMovie(child)
        return
    except MovieStopException:
        stopMovie(child)
        done()
    except subprocess.CalledProcessError, e:
        print "omxplayer output:", e.output

def sequentialPlay(path):
    movies = glob.glob(path)
    movies.sort()
    while 1:
        for movie in movies:
            playMovie(movie)
            time.sleep(2)

def randomPlay(path):
    movies = glob.glob(path)
    while 1:
        random.shuffle(movies)
        for movie in movies:
            playMovie(movie)
            time.sleep(2)

def checkForQuit():
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            return 1
    return 0

def done():
    pygame.display.quit()
    pygame.quit()
    sys.exit(0)


def sailorMoonClips():
    path = '/home/pi/sm/*.mp4'
    randomPlay(path)

def sailorMoonEpisodes():
    path = '/home/pi/sm/*.mp4'
    sequentialPlay(path)


try:
    screen = blackScreen()
    #pinkBox(screen)
    sailorMoonEpisodes()
    while 1:
        if checkForQuit():
            done()
        time.sleep(1)
except KeyboardInterrupt:
    print "ctrl+c"
    done()
except SystemExit:
    done()
