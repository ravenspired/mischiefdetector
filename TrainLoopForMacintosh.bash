#!/bin/bash

# ( I've modified it to work on my mac )
# TODO: Actually modify it

cd ~/Documents/GitHub\ Desktop/mischiefdetector
/opt/anaconda3/condabin/conda activate MischiefDetector
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
git commit -m 'Final Automated Training Commit of Session'
git pull
git push