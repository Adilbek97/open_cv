import cv2
import numpy as np
import threading
import time
import os
from PIL import Image
import datetime


class FaceDetector:
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('Classifiers/face.xml')
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 640)
        self.cam.set(4, 480)
        self.count = 0
        self.faceId = 0
        self.faces = None
        self.path = 'dataset'
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.names = list(i for i in range(20))

        self.quit = cv2.waitKey(30) & 0xff

    def show(self):
        self.reconizer = cv2.face.LBPHFaceRecognizer_create()
        self.reconizer.read('trainer/trainer.yml')
        while self.cam.isOpened():
            self.ret, self.img = self.cam.read()
            self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

            self.faces = self.faceCascade.detectMultiScale(
                self.gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(0.1*self.cam.get(3)), int(0.1*self.cam.get(4))),
            )

            for (x, y, w, h) in self.faces:
                cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                self.id, self.confidence = self.reconizer.predict(self.gray[y: y + h, x: x + w])

                if self.confidence < 100:
                    self.id = self.names[id]
                    self.confidence = '  {0}%'.format(round(100 - self.confidence))

                else:
                    self.id = 'unknown'
                    self.confidence = '  {0}%'.format(round(100 - self.confidence))

                cv2.putText(self.img, str(id), (x + 5, y - 5), self.font, 1, (255, 255, 255), 2)
                cv2.putText(self.img, str(self.confidence), (x + 5, y + h - 5), self.font, 1, (255, 255, 0), 1)

                if id == 3:
                    id += 1
                    self.addPhoto()
                    # agt = threading.Thread(target=self.addGetTraning)
                    # agt.start()


            cv2.imshow('camera', self.img)
            k = cv2.waitKey(10) & 0xff

            if k == 27:
                break

            # return self.faces



    def addPhoto(self):
        print('\n [INFO] Initializing face capture. Look the camera and wait ...')
        self.faceId += 1

        for (x, y, w, h) in self.faces:
            cv2.rectangle(self.img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            self.count += 1
            cv2.imwrite('dataset/Human.' + str(self.faceId) + '.' + str(self.count) + '.jpg', self.gray[y: y + h, x: x + w])
            cv2.imshow('image', self.img)
            if self.count >= 20:
                break
            print('\n [INFO] Compleate')
        return self.faceId



    def getDataset(self, path):
        self.imagePaths = [os.path.join(self.path, f) for f in os.listdir(self.path)]
        self.faceSamples = []
        self.ids = []

        for imagePath in self.imagePaths:
            pilImage = Image.open(imagePath).convert('L')
            imgNumpy = np.array(pilImage, 'uint8')
            id = int(os.path.split(imagePath)[-1].split('.')[1])

            self.faceTraning = self.faceCascade.detectMultiScale(imgNumpy)

            for (x, y, w, h) in self.faceTraning:
                self.faceSamples.append(imgNumpy[y: y + h, x: x + w])
                self.ids.append(id)

        return self.faceSamples, self.ids

    def traning(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        print('\n [Info] Trainig faces. if will take a few seconds. Wait ...')

        self.faceTraning, self.ids = self.getDataset(self.path)
        self.recognizer.train(self.faceTraning, np.array(self.ids))
        self.recognizer.write('trainer/trainer.yml')

        print('\n [INFO] {0} faces trained. Exiting Program'.format(len(np.unique(self.ids))))


    def addGetTraning(self):
        self.addPhoto()
        self.getDataset(self.path)
        self.traning()

    def run(self):
        # self.show()
        # self.getDataset(self.path)
        self.traning()

    def __del__(self):
        self.cam.release()
        cv2.destroyAllWindows()


f = FaceDetector()
# f.show()
f.run()
