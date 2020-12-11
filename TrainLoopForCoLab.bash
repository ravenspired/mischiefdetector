#!/bin/bash

# THIS SCRIPT WILL ONLY WORK IN GOOGLE COLAB
# ( unless you modify it to work elsewhere )

cd /content/mischiefdetector
/root/miniconda3/bin/conda activate MischiefDetectorpython
until read -t 3 -n 1; do
    echo '** SYNCING **'
    cp checkpoints/* /content/drive/My\ Drive/checkpoints
    cp /content/drive/My\ Drive/checkpoints/* /content/mischiefdetector/checkpoints

    echo '** TRAINING **'
    python ai/trainclassifier.py

    echo '** NEXT ROUND OF TRAINING **'
    echo '** PRESS ANY KEY TO CANCEL **'
done


echo '** FINAL SYNC **'
cp checkpoints/* '/content/drive/My Drive/checkpoints'