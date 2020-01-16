from PIL import ImageGrab
from PIL import Image
import time
import datetime
import os

def screenShot():
    while True:
        try:
            date = str(datetime.date.today())
            hour=str(datetime.datetime.now().strftime("%H"))
            os.makedirs("D:/mine/" + date + "/" + hour)
        except OSError,e:
            if e.errno != 17:
                raise
            time.sleep(1)
            pass
        while True:
            date = str(datetime.date.today())
            hour = str(datetime.datetime.now().strftime("%H"))
            date_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            img = ImageGrab.grab()
            FILES_DIR = 'mine'
            SAVE_PATH = "D:/"
            LOGFILE_NAME = "%s.png" % date_time
            LOGFILE_PATH = os.path.join(SAVE_PATH, FILES_DIR, LOGFILE_NAME)
            img.save(LOGFILE_PATH)
            break
        time.sleep(60)

screenShot()