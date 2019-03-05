import numpy as np
import serial
import cv2
import pyttsx3;
import time
data =serial.Serial('com5',9600)
def jan():
    data.write(bytes('1',"ascii"))
def och():
    data.write(bytes('0',"ascii"))
detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)
def saying(soz:str):#text to speech
  engine = pyttsx3.init();
  jan()
  engine.say(soz);
  engine.runAndWait();
  och()
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #print("x= ",x)
        print("y= ",len(faces))
        
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if(len(faces)>0):
            saying("Здравствуйте, у нас курсы по робототехнике,\
                   обучаем делать роботы, программированию, электронике. Можете записаться на бесплатный пробный урок.\
                   Знаете что я умею приготовить кофе для вас. А вы хотите сделать робота помошника и подарить маме? ")
            time.sleep(5)
    
cap.release()
cv2.destroyAllWindows()
