import sys, os
from time import sleep
import ai.classifier as mischief

def disablePrinting():
    sys.stdout = open(os.devnull, 'w')

def enablePrinting():
    sys.stdout = sys.__stdout__

SCREENCAP_DIR = "screencaps/"
mischief.load_from_checkpt()
mischief.compile_network()

while True:
    os.system("""screencapture -x """ + SCREENCAP_DIR + """subfolder/cap.png &> /dev/null""")

    # Take screenshots of all monitors
    # Saves the screenshots to "screencaps/subfolder/",
    # In order to simply and easily run the mischief detector on them
    #
    # The option -x takes the screenshot silently.

    mischiefs = []
    test_count = 16;

    for i in range(1, test_count):
        disablePrinting()
        results = mischief.predict_in_directory(SCREENCAP_DIR)
        enablePrinting()

        for index, image_info in results.iterrows():
            if image_info['class'] == 1:
                try:
                    # print("A1")
                    mischiefs[index] += 1
                except IndexError:
                    # print("B1")
                    mischiefs.append(1)
            else:
                try:
                    # print("A0")
                    mischiefs[index] += 0
                except IndexError:
                    # print("B0")
                    mischiefs.append(0)
            # print(str(index) + ": " + str(mischiefs[index]))

    disablePrinting()
    results = mischief.predict_in_directory(SCREENCAP_DIR)
    enablePrinting()
    for index, image_info in results.iterrows():
        # print(index)
        mischievousness = round(mischiefs[index] * 1000 / test_count) / 10
        print(image_info['file'] + ": " + str(mischievousness) + "% mischievous")
        if mischiefs[index] > test_count / 10:  # mischief threshhold is currently 1/10, or 10%
            os.system("say 'Mischief detected, " + str(mischievousness) + "%.'")
            os.system("cp " + SCREENCAP_DIR + image_info['file'] + " " + "savedcaps/$(date +%s)_" + str(index) + "_" + str(mischiefs[index]) + ".png")
        else:
            os.system("say 'No mischief detected.'")


    os.system("rm -f " + SCREENCAP_DIR + "subfolder/cap*.png")
