import cv2

import numpy as np

resim = cv2.imread("yuzler1.jpg")

yuz_casc=cv2.CascadeClassifier("face.xml")

griton = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
yuzler = yuz_casc.detectMultiScale(griton,1.1,4)
for (x,y,w,h) in yuzler:
    cv2.rectangle(resim,(x,y),(x+w,y+h),(0,255,0))

cv2.imshow('yuzler',resim)
cv2.waitKey(0)
cv2.destroyAllWindows()