import cv2
import numpy as np
import threading
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = 'face.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
id = 0
# names = ['qwerty', 'uiop', 'asdfh', 'jkl', 'zxcvbnm']
names = [i for i in range(20)]
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)
path = 'dataset'


def getImageAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')
        id = int(os.path.split(imagePath)[-1].split('.')[1])

        faces = faceCascade.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y: y + h, x: x + w])
            ids.append(id)

    return faceSamples, ids


face_id = 0
run_once = True


def face():
    global face_id

    while True:

        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, confidence = recognizer.predict(gray[y: y + h, x: x + w])

            if confidence < 100 and confidence > 0:
                id = names[id]
                confidence = '  {0}%'.format(round(100 - confidence))

            else:
                id = 'unknown'
                confidence = '  {0}%'.format(round(100 - confidence))

                if run_once:
                    count = 0
                    face_id += 1

                    for i in range(20):
                        for (x, y, w, h) in faces:
                            print(face_id)
                            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                            print(i)
                            count += i
                            cv2.imwrite('dataset/Human.' + str(face_id) + '.' + str(count) + '.jpg',
                                        gray[y: y + h, x: x + w])

                print('traning start')
                faces2, ids = getImageAndLabels(path)
                recognizer.train(faces2, np.array(ids))

                recognizer.write('trainer/trainer.yml')
                print('traning done')

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff

        if k == 27:
            print('\n [INFO] Exiting Program and cleanup stuff')
            cam.release()
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    face()
