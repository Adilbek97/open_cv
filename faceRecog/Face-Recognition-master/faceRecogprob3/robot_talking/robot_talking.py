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

        i=0
        while(i<1):
             bot.set_trainer(ListTrainer)
             bot.train(conv)
             i+=1

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


def saying(soz: str,surooBerdi):  # text to speech
    surooBerdi[1]=1
    engine = pyttsx3.init();
    engine.say(soz);
    engine.runAndWait();
    surooBerdi[1] = 0


def recog(r):  # speech to text

    with sr.Microphone(17) as source:
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


def listen_back(r):
    with sr.Microphone(5) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Skajite ")
        audio = r.listen(source, phrase_time_limit=2)
        try:

            return str(r.recognize_google(audio, language='Ru-ru'))
        except:
            return "oshibka boldu"
        # audio = r.listen_in_background(source,phrase_time_limit=1)


def joop_aluu(r, bot1, surooBerdi=None):
    print("joop aluu")
    suroo_jok1 = 0
    while True:
        word = str(input("suroo jaz..."))
        print(word)
        if (str(word) == 'null' or str(word) == 'oshibka'):
            print('suroo_jok= ', suroo_jok1)
            print("келди")
            suroo_jok1 += 1
            if (suroo_jok1 > 3):
                suroo_jok = 0
                break
        elif (word in askTime):
            suroo_jok1 = 0

            saying(currentTime())
        elif (word in askWeather):
            suroo_jok1 = 0
            saying(weather())
        else:
            suroo_jok1 = 0
            joop = bot1.answer(word)
            print(joop)
            saying(joop, surooBerdi)
# data = serial.Serial('com4', 9600)
def sendFaceCord(x:str,data):
    word=x
    for byte in word:
      data.write(bytes(byte,"ascii"))
    data.write(bytes(' ',"ascii"))
def sendData(val:str,data):
    data.write(bytes(val, "ascii"))
def suroo_joop(surooBerdi):
    r = sr.Recognizer()
    bot1 = Chatterbot()
    while True:
        try:
            surooBerdi[0] = 0
            # soz = listen_back(r)
            # print(soz)
            # if "робо" in soz:
            surooBerdi[0]=1
            saying("Здравствуйте, хотите чтото спросить.",surooBerdi)

            joop_aluu(r, bot1,surooBerdi)
        except:
            pass
if __name__ == '__main__':
    r = sr.Recognizer()
    bot1 = Chatterbot()
    while True:
        try:
            joop_aluu(r,bot1)
        except:
            pass

