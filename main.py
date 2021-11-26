import time

import pyautogui
import pyautogui as pyautogui


def fumo():
    flag = True
    while(flag):
        pyautogui.click(20, 20, clicks=1, interval=0.2, duration=0.2, button="left")
        location = pyautogui.locateCenterOnScreen("1.png   ", confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y, clicks=1, interval=0.2, duration=0.2, button="left")
            time.sleep(1)
            location = pyautogui.locateCenterOnScreen("2.png   ", confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=1, interval=0.2, duration=0.2, button="left")
            time.sleep(1)
            location = pyautogui.locateCenterOnScreen("3.png   ", confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=1, interval=0.2, duration=0.2, button="left")
            time.sleep(5)
        else:
            flag = False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        fumo()
