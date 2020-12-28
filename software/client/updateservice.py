#update file to minimize cloning the repo over and over onto the computers.

#At the moment, the update service will never receive updates. If this is a problem, please open an issue on GitHub.


import urllib.request, filecmp, sys, os, time



#INSECURE CODE: WORKAROUND UNTIL WE CAN SET UP ENCRYPTION CERTIFICATES
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#END OF INSECURE CODE


force_update = False #change to true to force an update
files_to_update = 3 #deprecated, will be removed


#Download check for updates file
print("Checking for updates...")
urllib.request.urlretrieve ("https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/client_version.txt", "sampleupdate.txt")#saves file as sampleupdate in current path


#Compare it with existing file
files = filecmp.cmp('originalupdate.txt', 'sampleupdate.txt', shallow=False)

if force_update == False:
	files = False


#Update if neccesary
if files == False:
    print("Updating Software...")
    time.sleep(1)
    print("Downloading updated files...")


    urllib.request.urlretrieve ("https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/imagecompressor.py", "imagecompressor_updated.py")
    urllib.request.urlretrieve ("https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/sendtoserver.py", "sendtoserver_updated.py")
    urllib.request.urlretrieve ("https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/service.py", "service_updated.py")#saves the update as a python file
    print("unpacking and replacing old files with new...")
    os.remove("originalupdate.txt")
    os.rename("sampleupdate.txt", "originalupdate.txt")
    os.remove("imagecompressor.py")
    os.remove("sendtoserver.py")
    os.remove("service.py")
    os.rename("imagecompressor_updated.py", "imagecompressor.py")
    os.rename("sendtoserver_updated.py", "sendtoserver.py")
    os.rename("service_updated.py", "service.py")

    print("Updated successfully.")

    


else:
    print("Up to date.")
    os.remove("sampleupdate.txt")

import service#run program as update check passed


#