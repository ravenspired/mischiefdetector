import os
import datetime


savetofile = "~/mischief_detector/temp_scrnsht/"+str(datetime.datetime.now())
savetofile= savetofile.replace(" ", "_")
savetofile= savetofile.replace(":", "_")
savetofile = savetofile.replace(".","_")
savetofile = savetofile + ".png"

print(savetofile)
os.system("screencapture "+savetofile)