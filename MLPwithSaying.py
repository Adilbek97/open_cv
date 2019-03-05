import time
import multiprocessing
import numpy as np
import cv2
import speech_recognition as sr
import pyttsx3;
import serial
from datetime import datetime as dt
import datetime
from chatterbot.trainers import ListTrainer #method to train the chatbot
from chatterbot import ChatBot
adamSany=0
#-------------------------Processes------------------------
def watching(v):
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while(True):
      ret, img = cap.read()
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = detector.detectMultiScale(gray, 1.3, 5)
      for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #print("x= ",x)
        print("y= ",len(faces))
        v.put(len(faces))
      cv2.imshow('frame',img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      #Array[0]=int(len(faces))
    cap.release()
    cv2.destroyAllWindows()

#----------------------------------------------------

class Chatterbot:#chat bot 
 def __init__(self):
     bot = ChatBot('Test')
     conv=open('chats.txt','r').readlines()
     #i=0
     #while(i<3):
     #bot.set_trainer(ListTrainer)
     #bot.train(conv)
      #i+=1

 def answer(self,soz:str):
    bot = ChatBot('Test')
    request=soz
    response=bot.get_response(request)
    #print(str(response))
    return response

def recog():#speech to text
 r = sr.Recognizer()
 with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Скажите что-нибудь")
        audio = r.listen(source,phrase_time_limit=3)
 try:
         return (r.recognize_google(audio, language="ru-RU"))
 except sr.UnknownValueError:
        print("Робот не расслышал фразу")
        return "null"
 except sr.RequestError as e:
        print("Ошибка сервиса; {0}".format(e))
        return "oshibka"
    
def saying(soz:str):#text to speech
  engine = pyttsx3.init();
  engine.say(soz);
  engine.runAndWait();
  #och()
def currentTime():
    month={1:"Январь",2:"Февраль",3:"Март",4:"Апрель",5:"Май",6:"Июнь",7:"Июль",8:"Август",9:"Сентябрь",10:"Октябрь",11:"Ноябрь",12:"Декабрь"}
    day={0:"Понедельник",1:"Вторник",2:"Вторник",3:"Среда",4:"Четверг",5:"Пятница",6:"Воскресенье"}
    now =dt.now()
    tday=datetime.date.today()
    word=str(now.year)+"й год "+str(now.day )+"й "+month[int(now.month)]+' '+day[int(tday.weekday())]+' '+str(now.hour)+" часов "+str(now.minute)+" минут "+str(now.second)+" секунд"
    return str(word)
def uploadFile():
    new_quetions.close()
    new_quetions=open('new_Asks.txt','a')
bot1=Chatterbot()
new_quetions=open('new_Asks.txt','a')
#data =serial.Serial('com4',9600)
def jan():
    data.write(bytes('1',"ascii"))
def och():
    data.write(bytes('0',"ascii"))
def fun(v):
 while True:   
   word=str(recog())
   print(word)
   if(str(word) == 'null' or str(word) == 'oshibka'):
     print("not ")
   else:
      joop=bot1.answer(word)
      print(joop)
      saying(joop)
   if(v.get()>0):
      print(v.get())
   
if __name__ == '__main__':
 sharedArray=multiprocessing.Array('i',1)
 v=multiprocessing.Queue()
 pros2=multiprocessing.Process(target=watching,args=(v,))
 pros2.start()
 pros1=multiprocessing.Process(target=fun(),args=(v,))
 pros1.start()

 pros2.join()
 pros1.join()

 


