import pyautogui
import time

def startapp(nameapp):
    pyautogui.hotkey('alt', 'f2')
    time.sleep(0.15)
    pyautogui.typewrite(nameapp)
    time.sleep(0.15)
    pyautogui.press('tab', 4, 0.1)
    pyautogui.press('enter')

def get_weather(PyOWM_var):
    w = PyOWM_var.weather_manager().weather_at_place('Kazan').weather
    temp = w.temperature(unit='celsius') #temperature
    tnow = temp['temp'] #now
    flike = temp['feels_like']
    det = w.detailed_status #like clouds etc.
    if 'clouds' in det:
        det = 'облачно'
    elif 'sun' in det:
        det = 'солнечно'
    elif 'rain' in det:
        det = 'дождливо'
    elif 'snow' in det:
        det = 'снег идет'
    wind = w.wind() #speed and deg
    wspeed, wdeg = wind['speed'], wind['deg']
    if wdeg>315 or wdeg<=45: wdeg = 'северный'
    elif wdeg>45 and wdeg<=135: wdeg = 'восточный'
    elif wdeg>135 and wdeg<=225: wdeg = 'южный'
    else: wdeg = "западный"
    return det, tnow, flike, wspeed, wdeg