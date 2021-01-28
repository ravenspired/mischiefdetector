#This script installs mischief detector onto your computer. It will also install updates, but it is recommended to use the updater

echo "Installation is now in progress."


mkdir ~/mischief_detector
mkdir ~/mischief_detector/temp/screenshots
mkdir ~/mischief_detector/unacceptable_scrnsht
touch ~/mischief_detector/mischief.log

curl https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/imagecapture.py --output ~/mischief_detector/imagecapture.py
curl https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/sendtoserver.py --output ~/mischief_detector/sendtoserver.py
curl https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/service.py --output ~/mischief_detector/service.py
curl https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/updateservice.py --output ~/mischief_detector/updateservice.py
curl https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/originalupdate.txt --output ~/mischief_detector/originalupdate.txt

echo "Installation completed."
