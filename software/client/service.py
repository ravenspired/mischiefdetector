#This is the main program that facilitates running the others. In other words, the logic loop.

from time import sleep
from random import randint

import updateservice
import imagecapture
import ai
import sendtoserver

SCREENCAP_DIR = "temp/"
MIN_DELAY_MINUTES = 2
MAX_DELAY_MINUTES = 5

#Program loop
while True:
    imagecapture.take_screenshot()
    detector.test_screenshot()
    sendtoserver.report_any_mischief()

    sleep(randint(MIN_DELAY_MINUTES*60, MAX_DELAY_MINUTES*60))

# This program should be run as root to avoid students killing it
