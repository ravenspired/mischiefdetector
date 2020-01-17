import os
import datetime
from PIL import Image
import os.path
homedir = os.path.expanduser("~")

print(homedir)
savetofile = homedir+"/mischief_detector/temp_scrnsht/"+str(datetime.datetime.now())
savetofile= savetofile.replace(" ", "_")
savetofile= savetofile.replace(":", "_")
savetofile = savetofile.replace(".","_")
savetofile = savetofile + ".png"

print(savetofile)
os.system("screencapture "+savetofile+" -x")


foo = Image.open(savetofile)
print(foo.size)
foo = foo.resize((129,72),Image.ANTIALIAS)
foo.save(savetofile+".png",quality=95)