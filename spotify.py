import os
import time

import pyautogui

from speak import speak
from speak import takecommand


def spotify():
    os.system("spotify")
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'l')
    speak("what song should i play")
    song = takecommand()
    pyautogui.write(song, interval=0.3)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.hotkey('enter')
