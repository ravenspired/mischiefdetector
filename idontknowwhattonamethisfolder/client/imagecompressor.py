import os
import datetime


savetofile = "screencapture ~/Documents/mischief_detector/temp_scrnshot/"+str(datetime.datetime.now())+".png"
savetofile.replace(" ", "_")
print(savetofile)
os.system(savetofile)