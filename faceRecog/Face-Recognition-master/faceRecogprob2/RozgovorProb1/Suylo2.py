import threading
import time
import random
import pyttsx3
import datetime

now = datetime.datetime.now()
minute = now.minute
print(minute)

birinchiSozdor = ["Привет", "как дело?", "Кто ты?", "Что ты хочешь"]
ekinchiSozdor = ["ПРивет", "Хорошо спасибо", "Меня зовут паланча", "Ничего"]


# print(birinchiSozdor[2])


def say1():
    print('func')
    engine = pyttsx3.init()
    voice = engine.getProperty("voices")
    engine.setProperty('voice', voice[2])

    while True:
        tmp = datetime.datetime.now().minute - minute
        print(tmp)
        rand = random.randint(0, 3)
        if (tmp == 1):
            print(datetime.datetime.now())
            engine.say(birinchiSozdor[rand])
            engine.runAndWait()
        elif (tmp == 0):
            engine.say(ekinchiSozdor[rand])
            engine.runAndWait()


say1()

# def say2():
#     print('func2')
#
#     while True:
#
#         print(datetime.datetime.now().minute - minute)
#         if ((datetime.datetime.now().minute - minute) == 3):
#             rand = random.randint(0, 3)
#             print(datetime.datetime.now())
#             engine = pyttsx3.init()
#             engine.say(ekinchiSozdor[rand])
#             engine.runAndWait()
#
#
# t = threading.Thread(target=say1, daemon=True)
# t.start()
# t2 = threading.Thread(target=say2, daemon=True)
# t2.start()
# t2.join()
# t.join()
