import sys, os
import ai.classifier as mischief


def disablePrinting():
    sys.stdout = open(os.devnull, 'w')


def enablePrinting():
    sys.stdout = sys.__stdout__


mischief.load_from_checkpt()
mischief.compile_network()


def test_screenshot(SCREENCAP_DIR, test_count=16, threshold=0.1):
    mischiefs = []

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
        if mischiefs[index] > test_count * threshold:  # mischief threshhold is currently 1/10, or 10%
            os.system("say 'Mischief detected, " + str(mischievousness) + "%.'")
            os.system("cp " + SCREENCAP_DIR + image_info['file'] + " " + "offending_screenshot.png")
        else:
            os.system("say 'No mischief detected.'")

    os.system("rm -f " + SCREENCAP_DIR + "screenshots/cap*.png")
