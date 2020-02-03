#This script installs files to your computer

echo "Installation is now in progress."


mkdir ~/mischief_detector
mkdir ~/mischief_detector/temp_scrnsht
mkdir ~/mischief_detector/unacceptable_scrnsht
touch ~/mischief_detector/mischief.log

curl https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/classifier/client/imagecompressor.py --output ~/mischief_detector/imagecompressor.py
curl https://raw.githubusercontent.com/ravenspired/mischiefdetector/master/classifier/server/server.py --output ~/mischief_detector


echo "Installation completed."

