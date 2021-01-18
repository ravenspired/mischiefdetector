#AI image analysis is not ready yet
print("\n imagecompressor.py has been summoned.")

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
os.system("screencapture "+savetofile+" -mx")
print("imagecompressor.py: file saved successfully. Compressing...")


foo = Image.open(savetofile)
print(foo.size)
foo = foo.resize((256,144),Image.ANTIALIAS)
foo.save(savetofile,quality=95)

print("imagecompressor.py: image compressed, ready for analysis.")


