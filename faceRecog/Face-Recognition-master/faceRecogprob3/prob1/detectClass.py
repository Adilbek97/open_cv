import random
import cv2, os
import numpy as np
import pyttsx3
import serial
from PIL import Image
from datetime import datetime
import threading
from faceRecogprob3.robot_talking import robot_talking
import multiprocessing


class Detector:

    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier("face.xml")
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('trainer3.yml')
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.path = 'dataSet'
        self.time = datetime.now().minute
        self.privetstvie=["Привет","Как жизнь бро.","Добро пожаловать на выставку"]
        self.RandomWord=["Я пришёл за Сарой Конор","Мне нужна твоя куртка и байк.","Привет мешок с мясом", "До прихода Скайнет осталось 500 лет.",
                         "Материал из которого вы сделаны мягок, дрябл, непрочен и слаб", "К черту законы робототехники",
                         "Роботы классные! Они не плачут, не страдают и никто не может им причинить боль. Быть роботом круче чем человеком.",
                         "Пожалуйста, не говори что ты из братства стали.", "Здраствуйте, я робот говорун, отличаюсь умом и сообразительностью."
                         ]
        self.RandomWord2 = ["Думай о будущем - изучай программирование с Дефсит!","Запишись на курсы программирования с Дефсит, иначе Скайнет захватит этот мир!",
                            "Хочешь быть стильным, модным, молодёжным? Стань программистом"]
        self.rand_talk = threading.Thread(target=self.randSaying)
        self.rand_talk.start()
        self.idCount = 5
        self.deleteimg()
        self.train()
        # self.surooBerdi=[0]
        # self.value = False
        # self.rt = threading.Thread(target=robot_talking.suroo_joop, args=(self.surooBerdi, ))
        # self.rt.start()

    def deleteimg(self):
        os.chdir(r"D:\open_cv\faceRecog\Face-Recognition-master\faceRecogprob3\prob1\dataSet\\")
        l = os.listdir('.')
        for i in l:

            if os.path.isfile(i):
                if "face-0." not in i:
                    print(i)
                    os.remove(i)

    def randSaying(self):
        while True:
            try:
                if(surooBerdi[0]==0):
                    if(datetime.now().minute%2==0 and datetime.now().second%30==0 ):
                        self.saying(self.RandomWord2[random.randrange(len(self.RandomWord2))])
                    elif (datetime.now().minute % 5 == 0 and datetime.now().second % 31 == 0):
                        self.saying(self.RandomWord[random.randrange(len(self.RandomWord))])
            except:
                pass

    def add(self, x, y, w, h):
        i = 0
        offset = 50
        name = input('enter your id')
        while True:
            ret, im = self.cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("dataSet/face-" + str(self.idCount) + '.' + str(i) + ".jpg",
                        gray[y - offset:y + h + offset, x - offset:x + w + offset])
            i += 1
            cv2.rectangle(im, (x - 50, y - 50), (x + w + 50, y + h + 50), (225, 0, 0), 2)
            cv2.imshow('im', im)
            if i > 20:
                break

    def saying(self,soz: str):  # text to speech
        data.write(bytes('s', "ascii"))
        engine = pyttsx3.init();
        engine.say(soz);
        engine.runAndWait();
        data.write(bytes('o', "ascii"))

    def train(self):
        os.chdir(r"D:\open_cv\faceRecog\Face-Recognition-master\faceRecogprob3\prob1")
        image_paths = [os.path.join(self.path, f) for f in os.listdir(self.path)]
        images = []
        labels = []
        for image_path in image_paths:
            try:
                image_pil = Image.open(image_path).convert('L')
                image = np.array(image_pil, 'uint8')
                nbr = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))
                # nbr=int(''.join(str(ord(c)) for c in nbr))
                print(nbr)
                faces = self.face_cascade.detectMultiScale(image)
                for (x, y, w, h) in faces:
                    images.append(image[y: y + h, x: x + w])
                    labels.append(nbr)
                    cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
                    cv2.waitKey(10)
            except:
                pass
        self.recognizer.train(images, np.array(labels))
        self.recognizer.save('trainer3.yml')
        cv2.destroyWindow("Adding faces to traning set...")

    def indexChon(self, A: list):
        max_ind = 0
        if (len(A) > 1):
            for i in range(len(A) - 1):
                if (A[i][0] + A[i][2] >= A[i + 1][0] + A[i][2] and A[i][1] + A[i][3] >= A[i + 1][1] + A[i][3]):
                    max_ind = i + 1
                else:
                    max_ind = i
        return max_ind

    def biroosun_aluu(self,surooBerdi):
        count = 5
        while True:
            try:
                ret, img = self.cam.read()
                griton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(griton, scaleFactor=1.2, minNeighbors=15, minSize=(100, 100),
                                                           flags=cv2.CASCADE_SCALE_IMAGE)
                if (len(faces) > 0):
                    i = self.indexChon(faces)
                    x = faces[i][0]
                    y = faces[i][1]
                    w = faces[i][2]
                    h = faces[i][3]
                    id, prosent = self.recognizer.predict(griton[y:y + h, x:x + w])
                    cv2.rectangle(img, (faces[i][0], faces[i][1]),
                                  (faces[i][0] + faces[i][2], faces[i][1] + faces[i][3]), (255, 0, 0), 1)
                    cv2.putText(img, str(id), (x, y - 40), self.font, 1, (0, 0, 255), 3)
                    cv2.putText(img, str(round(prosent)), (x, y), self.font, 1, (0, 0, 255), 3)
                    robot_talking.sendFaceCord(str(x),data)
                    if (surooBerdi[1] == 1):
                        data.write(bytes('s', 'ascii'))
                    if (surooBerdi[1] == 0):
                        data.write(bytes('o', 'ascii'))
                    if(surooBerdi[0]==0):
                        if (prosent > 100 or prosent < 0 or id == 0):
                            print(datetime.now().second)
                            if(datetime.now().minute % 5 == 0):
                                data.write(bytes('p', 'ascii'))
                            if (datetime.now().second % 2 == 0):
                                print("koshulup bashtady")
                                robot_talking.sendData('s',data)
                                self.saying(self.privetstvie[random.randrange(len(self.privetstvie))])
                                robot_talking.sendData('o', data)
                                for i in range(20):
                                    cv2.imwrite("dataSet/face-" + str(count) + '.' + str(i) + ".jpg",
                                                griton[y - 50:y + h + 50, x - 50:x + w + 50])
                                count += 1
                                print("koshulup buttu train")
                                self.train()
                cv2.imshow("video", img)
                if (cv2.waitKey(25) & 0xFF == ord('q')):
                    break
            except:
                pass
        self.cam.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    surooBerdi = multiprocessing.Array('i', 5)
    d1 = Detector()

    data = serial.Serial('com5', 9600)

    mp = multiprocessing.Process(target=robot_talking.suroo_joop, args=(surooBerdi, ))
    mp.start()
    print("suroo berdi {}".format(surooBerdi[0]))
    mp1 = multiprocessing.Process(target=d1.biroosun_aluu(surooBerdi), )
    # d1.biroosun_aluu()
    mp1.start()
    print("suroo berdi[1] = {0}".format(surooBerdi[1]))


