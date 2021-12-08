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

#variables

owmap = pyowm.OWM('44e45e2833d1c08430d69d5a7c59ac39')

wait_mode = False

r = sr.Recognizer()

#program main work
if os.stat("./Linux/config.ini").st_size == 0:
    firstConfig()

if os.stat("./Linux/config.ini").st_size == 0:
    exit()
        

def getinfo():
    try:
        with sr.Microphone() as m:
            r.adjust_for_ambient_noise(m)
            print("Speak")
            aud = r.listen(m)
            recognized_all = [i.lower() for i in r.recognize_google(
                aud, language='ru-RU', show_all=True)]
    except sr.UnknownValueError:
        speak("не удалось распознать речь")
    except sr.RequestError:
        speak("Неизвестеная ошибка. Проверьте подключение к интернету")

    for voice in recognized_all:
        task, args = callback(voice)
        if not (task == 0 and args == 0):
            break
    exec(task, args)


def callback(v):
    for name in alias['names']:
        if name in v:
            v = v.replace(name, '')
            for op in alias['cmds']:
                if op == 'media_ctrl':
                    for inner_op in alias['cmds']['media-ctrl']:
                        for cmd in alias['cmds']['media-ctrl'][inner_op]:
                            if cmd in v:
                                task = inner_op
                                args = v.replace(cmd, '')
                                print(args)
                                return task, args
                else:
                    for cmd in alias['cmds'][op]:
                        if cmd in v:
                            task = op
                            args = v.replace(cmd, '')
                            print(args)
                            return task, args
            else:
                return 0, 0
    else:
        return 0, 0


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
            webbrowser.get(using=browser).open_new_tab(
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
                volume_change(change=(-1)**((task == 'vol-up')+1)*int(args[-3:]))
        elif task=='play' or task=='pause':
            subprocess.call(['playerctl', 'play-pause'])
        elif task=='wait':
            wait_mode = True
    else:
        if task=='start':
            wait_mode = False



getinfo()
