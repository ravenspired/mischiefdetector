#update file to minimize cloning the repo over and over onto the computers.



import urllib.request, filecmp, sys, os, time


#Download check for updates file
print("Checking for updates...")
urllib.request.urlretrieve ("https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/client_version.txt", "sampleupdate.txt")#saves file as sampleupdate in current path


#Compare it with existing file
files = filecmp.cmp('originalupdate.txt', 'sampleupdate.txt', shallow=False)



#Update if neccesary
if files == False:
    print("Updating Software...")
    time.sleep(1)
    urllib.request.urlretrieve ("http://host.com/updatedsoftware.script", "update.py")#saves the update as a python file
    os.remove("originalupdate.txt")
    os.rename("sampleupdate.txt", "originalupdate.txt")
    os.remove("service.py")
    os.rename("update.py", "service.py")


else:
    print("Up to date.")
    os.remove("sampleupdate.txt")

import service#run program as update check passed