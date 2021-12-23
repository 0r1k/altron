import pyaudio
from pyowm import owm
import speech_recognition as sr
import os
import pyautogui
import pyowm
import webbrowser
from config import *
import subprocess
import time
from functions import *
import configparser
import asyncio

#variables

owmap = pyowm.OWM('44e45e2833d1c08430d69d5a7c59ac39')

wait_mode = False

#program main work
if os.stat("./config.ini").st_size == 0:
    firstConfig(conf)

if os.stat("./config.ini").st_size == 0:
    exit()        

def getinfo():
    task, args = 0, 0
    try:
        with sr.Microphone() as m:
            r.adjust_for_ambient_noise(m)
            print("SAY")
            audio = r.listen(m)
        l = r.recognize_google(audio, language='ru-RU', show_all=True)
        # print("Func:", l['alternative'])
        if type(l)!=list:
            recognized_all = [var['transcript'].lower() for var in l['alternative']]
        else:
            return
        print(*recognized_all, sep='\n')
    except sr.UnknownValueError:
        speak("не удалось распознать речь")
    except sr.RequestError:
        speak("Неизвестеная ошибка. Проверьте подключение к интернету")
    if recognized_all==[]:
        return
    voice_num = 0
    print(task, args)
    while task==0 and args==0:
        voice_num += 1
        if voice_num==len(recognized_all):
            return
        task, args = callback(recognized_all[voice_num], alias)
    # print(task, args)
    exec(task, args)





def exec(task, args):
    global wait_mode
    if task == 0:
        pass
    elif not wait_mode:
        if task == 'weather':
            det, tnow, flike, wspeed, wdeg = get_weather(PyOWM_var=owmap)
            print(det, tnow, flike, wspeed, wdeg)
            speak(f"""{det}, {int(tnow)} градусов, ощущается как {int(flike)}. Ветер {wdeg}, {int(wspeed)} метров в секунду""")
        elif task == 'google':
            webbrowser.get(using=conf.get("DEFAULT", 'browser')).open_new_tab(
                'https://www.google.com/search?q='+args)
        elif task == 'open':
            for anm in ['программу', 'приложение']:
                if anm in args:
                    args.replace(anm, '')
            startapp(args.strip())
        elif task.startswith('vol'):
            if 'до' in args:
                volume_change(int(args[-3:]))
            elif 'на' in args:
                volume_change(change=(-1)**((task == 'vol-down'))*int(args[-3:]))
        elif task=='play' or task=='pause':
            subprocess.call(['playerctl', 'play-pause'])
        elif task=='wait':
            wait_mode = True
    else:
        if task=='start':
            speak("К вашим услугам, {}".format(conf.get("DEFAULT", 'name')))
            wait_mode = False

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)

while True:
    getinfo()