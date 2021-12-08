import configparser

from keyboard import is_pressed
from functions import speak

conf = configparser.ConfigParser()

alias = {
    "names": ["альтрона", "альтрон"],
    'cmds': {
        'weather': ['погода', "погоду"],
        'google': ['интернет', 'браузер', 'загугли', "найди", "гугл", "google"],
        'open': ['открой программу', 'открой приложение', 'открой',
                 'запусти', 'запусти программу', 'запусти приложение', ],
        'media-ctrl': {
            'pause': ['пауза', 'паузу'],
            'play': ['воспроизведи', 'играй', 'продолжай', ],
            'next': ['следующее', 'дальше', 'следующий', 'следующую'],
            'prev': ['прошлое', 'прошлый', 'прошлую'],
            'vol-down': ['убавь', 'уменьши'],
            'vol-up': ['прибавь'],
            'rewind':['перемотай', 'мотни'],
        },
        'wait': ['подожди', 'жди', 'выклюючись'],
        'start': ['ты тут'],
    },
}


def firstConfig():
    speak("""Введите некоторую информацию для начала работы.
    Нажмите клавишу Enter, чтобы продолжить или клавишу esc, чтобы закрыть программу""")
    if is_pressed('enter'):
        pass
    elif is_pressed('esc'):
        return
    speak("Как к вам обращаться?")
    conf.set('DEFAULT', 'name', input())
    speak("Какой вы браузер используете? Напишите его название на английском")
    conf.set('DEFAULT', 'browser', input())
    speak("В каком вы городе живёте? Напишите его название на английском")
    conf.set('DEFAULT', 'city', input())
    #adding to the file
    f = open("./Linux/config.ini", 'w')
    conf.write(f)