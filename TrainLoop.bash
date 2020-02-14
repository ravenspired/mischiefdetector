#!/bin/bash

# THIS SCRIPT WILL ONLY WORK IN GOOGLE COLAB
# ( unless you modify it )

cd /content/mischiefdetector
/root/miniconda3/bin/conda activate MischiefDetectorpython
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