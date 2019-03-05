import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

yuz_casc=cv2.CascadeClassifier("face.xml")

while True:
    ret,frame = kamera.read()
    griton = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler = yuz_casc.detectMultiScale(griton,1.1,4)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('orijinal',frame)
    if (cv2.waitKey(25) & 0xFF ==ord('q')):
        break
kamera.release()
cv2.destroyAllWindows()


