#!/bin/bash

# ( I've modified it to work on my mac )
# TODO: Actually modify it

cd ~/Documents/GitHub/mischiefdetector
source /opt/anaconda3/bin/activate MischiefDetector
until read -t 3 -n 1; do
    echo '** SYNCING **'
    git add -A
    git commit -m 'Automated Training Commit'
    git pull
    git push

    echo '** TRAINING **'
    python ai/trainclassifier.py

    echo '** NEXT ROUND OF TRAINING **'
    echo '** PRESS ANY KEY TO CANCEL **'
done


echo '** FINAL SYNC **'
git add -A
git commit -m 'Automated Training Commit (End of Session)'
git pull
git push