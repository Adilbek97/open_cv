import cv2,os
import numpy as np
from PIL import Image 
import pickle

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX #Creates a font
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        if(nbr_predicted==7):
             nbr_predicted='Obama'
        elif(nbr_predicted==2):
             nbr_predicted='Robot'
        elif(nbr_predicted==1):
             nbr_predicted='Adilbek'
        elif(nbr_predicted==3):
             nbr_predicted='Bayram'
        else:
             nbr_predicted='unknow'
        cv2.putText(im, str(nbr_predicted)+"--"+str(conf), (x,y-40), font, 1, (255,255,255), 3)
        #out.write(im)
        cv2.imshow('im',im)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.waitKey(1)
cam.release()
#out.release()
cv2.destroyAllWindows()









