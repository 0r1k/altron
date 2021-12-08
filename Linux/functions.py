import pyautogui
import time
import subprocess
import re
import os
from config import conf

def speak(what):
    os.system("echo {} | RHVoice-test -p Aleksandr".format(what))

def startapp(nameapp):
    pyautogui.hotkey('alt', 'f2')
    time.sleep(0.15)
    pyautogui.typewrite(nameapp)
    time.sleep(0.15)
    pyautogui.press('tab', 4, 0.1)
    pyautogui.press('enter')


def get_weather(PyOWM_var):
    w = PyOWM_var.weather_manager().weather_at_place(conf.get("DEFAULT", 'city')).weather
    temp = w.temperature(unit='celsius')  # temperature
    tnow = temp['temp']  # now
    flike = temp['feels_like']
    det = w.detailed_status  # like clouds etc.
    if 'clouds' in det:
        det = 'облачно'
    elif 'sun' in det:
        det = 'солнечно'
    elif 'rain' in det:
        det = 'дождливо'
    elif 'snow' in det:
        det = 'снег идет'
    wind = w.wind()  # speed and deg
    wspeed, wdeg = wind['speed'], wind['deg']
    if wdeg > 315 or wdeg <= 45:
        wdeg = 'северный'
    elif wdeg > 45 and wdeg <= 135:
        wdeg = 'восточный'
    elif wdeg > 135 and wdeg <= 225:
        wdeg = 'южный'
    else:
        wdeg = "западный"
    return det, tnow, flike, wspeed, wdeg


def volume_change(to_value=-1, change=0):
    if to_value != -1:
        subprocess.run(
            ['amixer', '-D', 'pulse', 'sset', 'Master', str(to_value)])
    else:
        getval = subprocess.getoutput(
            ['amixer', '-D', 'pulse', 'sget', 'Master'])
        level_was = int(re.findall('Playback.+\d{2,3}%', getval)[0][-3:-1])
        subprocess.run(['amixer', '-D', 'pulse', 'sset',
                       'Master', str(level_was+change)])

#net search is in main.py file 'cause there's only 1-2 strokes