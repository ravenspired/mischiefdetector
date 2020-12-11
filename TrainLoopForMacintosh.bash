#!/bin/bash

# ( I've modified it to work on my mac )
# Run this using source or .
# Or, if running it by other means,
# ensure your .bash_profile is executed first,
# in the same bash instance.
# This is necessary for conda to initialize itself properly.
# Otherwise, the "conda" command below will throw a command not found error.

# Also, be sure to run this from the root directory
# of the mischiefdetector project,
# or specify the path using the mischiefLocation variable.

[ "$mischiefLocation" ] && cd "$mischiefLocation"
conda activate MischiefDetector
until read -t 3 -n 1; do
    echo '** SYNCING **'
    git add -A
    git commit -m 'Automated Training Commit'
    git pull --no-edit
    git push

    echo '** TRAINING **'
    python ai/trainclassifier.py

    echo '** NEXT ROUND  OF TRAINING **'
    echo '** PRESS ANY KEY TO CANCEL **'
done


echo '** FINAL SYNC **'
git add -A
git commit -m 'Automated Training Commit (End of Session)'
git pull --no-edit
git push
