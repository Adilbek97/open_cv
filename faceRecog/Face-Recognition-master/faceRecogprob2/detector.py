import cv2, os
import numpy as np
from PIL import Image
import pickle
import dataSetGenerator2
import threading

# def dataSetGenerator(cam):
#     detector = cv2.CascadeClassifier('Classifiers/face.xml')
#     i = 0
#     offset = 50
#     name = input('enter your id')
#     while True:
#         ret, im = cam.read()
#         gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#         faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100),flags=cv2.CASCADE_SCALE_IMAGE)
#         for (x, y, w, h) in faces:
#             i = i + 1
#             cv2.imwrite("../dataSet/face-" + name + '.' + str(i) + ".jpg",
#                         gray[y - offset:y + h + offset, x - offset:x + w + offset])
#             cv2.rectangle(im, (x - 50, y - 50), (x + w + 50, y + h + 50), (225, 0, 0), 2)
#             cv2.imshow('im', im[y - offset:y + h + offset, x - offset:x + w + offset])
#             cv2.waitKey(100)
#         if i > 20:
#             cam.release()
#             cv2.destroyAllWindows()
#             break


fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer2.yml')
cascadePath = "../Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX  # Creates a font

while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y + h, x:x + w])

        cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
        if (nbr_predicted == 0):
            # t = threading.Thread(target=dataSetGenerator2.add, daemon=True, args=(cam,))
            # t.start()
            # dataSetGenerator2.add(cam)

            # dataSetGenerator2.add(cam)
            nbr_predicted = 'Taanybaim'
        elif (nbr_predicted == 9):
            # dataSetGenerator2.add(cam)
            nbr_predicted = 'Sanjar'

        # elif (nbr_predicted == 2):
        #     nbr_predicted = 'Robot'
        # elif (nbr_predicted == 1):
        #     nbr_predicted = 'Adilbek'
        # elif (nbr_predicted == 3):
        #     nbr_predicted = 'Bayram'
        # else:
        #     nbr_predicted = 'unknow'
        cv2.putText(im, str(nbr_predicted), (x, y - 40), font, 1, (255, 255, 255), 3)
        # out.write(im)
    cv2.imshow('im', im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.waitKey(1)
cam.release()
# out.release()
cv2.destroyAllWindows()
