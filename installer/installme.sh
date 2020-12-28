#This script installs files to your computer

echo "Installation is now in progress."


mkdir ~/mischief_detector
mkdir ~/mischief_detector/temp_scrnsht
mkdir ~/mischief_detector/unacceptable_scrnsht
touch ~/mischief_detector/mischief.log

curl https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/imagecompressor.py --output ~/mischief_detector/imagecompressor.py
curl https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/client/sendtoserver.py --output ~/mischief_detector/sendtoserver.py
curl https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/server/service.py --output ~/mischief_detector/service.py
curl https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/software/server/updateservice.py --output ~/mischief_detector/updateservice.py

echo "Installation completed."
