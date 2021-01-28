#This is the main program that facilitates running the others. In other words, the logic loop.


import updateservice
import imagecapture
import ai
import sendtoserver

SCREENCAP_DIR = "temp/"

#Program loop
while True:
    imagecapture.take_screenshot()
    detector.test_screenshot()
    sendtoserver.report_any_mischief()



#program should be run as root to avoid students killing it
