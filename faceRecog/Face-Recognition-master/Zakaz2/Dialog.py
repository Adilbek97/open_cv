import speech_recognition as sr
import pyttsx3
import serial
import datetime
from datetime import datetime as dt
import requests
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class Chatterbot:  # chat bot
    def __init__(self):
        bot = ChatBot('Test')
        conv = open('chats.txt', 'r').readlines()

        # i=0
        # while(i<4):
        #     bot.set_trainer(ListTrainer)
        #     bot.train(conv)
        #     i+=1

    def answer(self, soz: str):
        bot = ChatBot('Test')
        request = soz
        response = bot.get_response(request)
        # print(str(response))
        return response


# ------------------------------------suroo listter---------------------

askTime = ["Сколько времени сейчас?", "Который час?", "сколько времени сейчас?", "который час?",
           "сколько сейчас времени?",
           "Сколько сейчас времени?", "Сколько время сейчас?", "сколько время сейчас?",
           "Сколько времени сейчас", "Который час", "сколько времени сейчас", "который час",
           "сколько сейчас времени", "Сколько сейчас времени", "Сколько время сейчас", "сколько время сейчас",
           ]
askWeather = ["какая сегодня погода?", "Какая сегодня погода?", "Погода сегодня какая?", "погода сегодня какая?",
              "какая сегодня погода", "Какая сегодня погода", "Погода сегодня какая", "погода сегодня какая"]


# ----------------------------------------------------------------------


def currentTime():
    month = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
             9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
    day = {0: "Понедельник", 1: "Вторник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Воскресенье"}
    now = dt.now()
    tday = datetime.date.today()
    word = str(now.year) + "й год " + str(now.day) + "й " + month[int(now.month)] + ' ' + day[
        int(tday.weekday())] + ' ' + str(now.hour) + " часов " + str(now.minute) + " минут " + str(
        now.second) + " секунд"
    return str(word)


def weather():
    word = "сейчас "
    url = 'http://api.apixu.com/v1/current.json?key=775f00d9a2754b1e9c0130256182106&q=Bishkek%20Kyrgyzstan'
    response = requests.get(url)
    temp = (response.json())
    print(temp['current']['temp_c'])
    word += str(int(temp['current']['temp_c'])) + " градус сельций"
    return word


def saying(soz: str,data):  # text to speech
    engine = pyttsx3.init();
    data.write(bytes('1', "ascii"))
    engine.say(soz);
    engine.runAndWait();
    data.write(bytes('0', "ascii"))


def recog(r):  # speech to text

    with sr.Microphone(0) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Скажите что-нибудь")
        audio = r.listen(source, phrase_time_limit=3)
    try:
        return (r.recognize_google(audio, language="ru-RU"))
    except sr.UnknownValueError:
        print("Робот не расслышал фразу")
        return "null"
    except sr.RequestError as e:
        print("Ошибка сервиса; {0}".format(e))
        return "oshibka"


def joop_aluu(r, bot1,data):
    print("joop aluu")
    while True:
        word = str(recog(r))
        print(word)
        if (str(word) == 'null' or str(word) == 'oshibka'):
            print('suroo_jok= ')
            print("келди")
        elif (word in askTime):
            saying(currentTime(),data)
        elif (word in askWeather):
            saying(weather(),data)
        else:
            joop = bot1.answer(word)
            print(joop)
            saying(joop,data)


def suroo_joop():
    r = sr.Recognizer()
    bot1 = Chatterbot()

    while True:
        try:
            joop_aluu(r, bot1)
        except:
            pass


if __name__ == '__main__':
    data = serial.Serial('com4', 9600)
    r = sr.Recognizer()
    bot1 = Chatterbot()
    while True:
        try:
            joop_aluu(r, bot1,data)
        except:
            pass
