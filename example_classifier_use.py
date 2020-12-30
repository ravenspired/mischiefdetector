import os
import ai.classifier as mischief
from pandas import DataFrame
import numpy as np

os.system("""  # This shell script takes screenshots of monitors
               # until it runs out of monitors.
  screenNum=1
  while screencapture -xD $screenNum screencaps/subfolder/cap${screenNum}.png
  do
    screenNum=$((screenNum+1))
  done
""")

# Take screenshots of all monitors
# Saves the screenshots to "screencaps/subfolder/",
# In order to simply and easily run the mischief detector on them
#
# The option -x takes the screenshot silently.

mischief.load_from_checkpt()
mischief.compile_network()
results = mischief.predict_in_directory("screencaps/")

for a, b in results.items():
    print(a)
