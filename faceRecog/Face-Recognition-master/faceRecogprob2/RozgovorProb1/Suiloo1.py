import pyttsx3
import datetime
import win32com.client

def date():
    dt5 = datetime.timedelta(minutes=27)
    return dt5

def suyloo(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()




