import configparser

from keyboard import is_pressed
from functions import speak

conf = configparser.ConfigParser()

alias = {
    "names": ["альтрона", "альтрон"],
    'cmds': {
        'scenarios':{
            'add':['добавь сценарий', 'создай сценарий', 'новый сценарий'],
            'open':['запусти сценарий', 'начни сценарий', 'запусти сценарий', ]
        },
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


def firstConfig(confile):
    speak("""Введите некоторую информацию для начала работы.
    Нажмите клавишу Enter, чтобы продолжить или клавишу esc, чтобы закрыть программу""")
    if is_pressed('enter'):
        pass
    elif is_pressed('esc'):
        return
    speak("Как к вам обращаться?")
    name = input()
    speak("Какой вы браузер используете? Напишите его название на английском")
    browser = input()
    speak("В каком вы городе живёте? Напишите его название на английском")
    city = input()
    confile['DEFAULT'] = {
        'name': name,
        'browser': browser,
        'city': city,
    }
    #adding to the file
    with open('config.ini', 'w') as f:
        confile.write(f)