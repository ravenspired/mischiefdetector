#update file to minimize cloning the repo over and over onto the computers.

#At the moment, the update service will never receive updates. If this is a problem, please open an issue on GitHub.

print("\nupdateservice.py has been summoned.")
import urllib.request, filecmp, sys, os, time
import os.path
from os import path


#INSECURE CODE: WORKAROUND UNTIL WE CAN SET UP ENCRYPTION CERTIFICATES
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#END OF INSECURE CODE


force_update = False #change to true to force an update
files_to_update = 3 #deprecated, will be removed


#Download check for updates file
print("updateservice.py: checking for updates...")
urllib.request.urlretrieve ("https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/client_version.txt", "sampleupdate.txt")#saves file as sampleupdate in current path


#Compare it with existing file
files = filecmp.cmp('originalupdate.txt', 'sampleupdate.txt', shallow=False)

if force_update == False:
	files = False

#EASTER EGG LMAO LOL

if path.exists("imagecapture.py"):
    print("Woah - This client is way out of date - ALL OF ITS FILES ARE MISSING!")

else:
    print("\n")

    #do nothing, continue the service loop 






#Update if neccesary
if files == False:
    print("updateservice.py: updating software...")
    time.sleep(1)
    print("updateservice.py: downloading updated files...")


    urllib.request.urlretrieve ("https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/imagecapture.py", "imagecapture_updated.py")
    urllib.request.urlretrieve ("https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/sendtoserver.py", "sendtoserver_updated.py")
    urllib.request.urlretrieve ("https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/service.py", "service_updated.py")#saves the update as a python file
    print("updateservice.py: unpacking and replacing old files with new...")
    os.remove("originalupdate.txt")
    os.rename("sampleupdate.txt", "originalupdate.txt")
    os.remove("imagecapture.py")
    os.remove("sendtoserver.py")
    os.remove("service.py")
    time.sleep(5)
    os.rename("imagecapture_updated.py", "imagecapture.py")
    os.rename("sendtoserver_updated.py", "sendtoserver.py")
    os.rename("service_updated.py", "service.py")

    print("updateservice.py: updated successfully.")

    


else:
    print("Up to date.")
    os.remove("sampleupdate.txt")



#