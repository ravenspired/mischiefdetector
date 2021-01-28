print("\nimagecapture.py has been summoned.")

import os
import datetime
import os.path
homedir = os.path.expanduser("~")

print(homedir)
savetofile = homedir+"/mischief_detector/temp/screenshots/"+str(datetime.datetime.now())
savetofile= savetofile.replace(" ", "_")
savetofile= savetofile.replace(":", "_")
savetofile = savetofile.replace(".","_")
savetofile = savetofile + ".png"


print(savetofile)
os.system("screencapture "+savetofile+" -mx")
print("imagecapture.py: file saved successfully.")


# foo = Image.open(savetofile)
# print(foo.size)
# foo = foo.resize((256,144),Image.ANTIALIAS)
# foo.save(savetofile,quality=95)

# print("imagecapture.py: image compressed, ready for analysis.")
