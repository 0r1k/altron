import pyaudio
from pyowm import owm
import pyttsx3
import speech_recognition as sr
import os
import pyautogui
import pyowm
import webbrowser
from config import *
import subprocess
import time
from functions import *

print(alias['names'])

#variables
owmap = pyowm.OWM('44e45e2833d1c08430d69d5a7c59ac39')
e = pyttsx3.init()
vs = e.getProperty('voices')
e.setProperty('voice', 'ru')
e.setProperty('rate', 50)

r = sr.Recognizer()

def speak(what):
    os.system("echo {} | RHVoice-test -p Aleksandr".format(what))

def getinfo():
    try:
        with sr.Microphone() as m:
            r.adjust_for_ambient_noise(m)
            print("Speak")
            aud = r.listen(m)
            recognized_all = [i.lower() for i in r.recognize_google(aud, language='ru-RU', show_all=True)]
    except sr.UnknownValueError:
        speak("не удалось распознать речь")
    except sr.RequestError:
        speak("Неизвестеная ошибка. Проверьте подключение к интернету")
    
    for voice in recognized_all:
        task, args = callback(voice)
        if not (task==0 and args==0):
            break
    exec(task, args)

def callback(v):
    for name in alias['names']:
        if name in v:
            v = v.replace(name, '')
            for op in alias['cmds']:
                for cmd in alias['cmds'][op]:
                    if cmd in v:
                        task = op
                        args = v.replace(cmd, '')
                        print(args)
                        return task, args
            else:
                return 0,0
    else:
        return 0,0

def exec(task, args):
    if task==0:
        pass  
    elif task=='weather':
        det, tnow, flike, wspeed, wdeg = get_weather(PyOWM_var=owmap)
        print(det, tnow, flike, wspeed, wdeg)
        speak(f"""{det}, {int(tnow)} градусов, ощущается как {int(flike)}. Ветер {wdeg}, {int(wspeed)} метров в секунду""")
    elif task=='google':
        webbrowser.get(using=browser).open_new_tab('https://www.google.com/search?q='+args)
    elif task=='open':
        for anm in ['программу', 'приложение']:
            if anm in args:
                args.replace(anm, '')
        startapp(args.strip())


getinfo()