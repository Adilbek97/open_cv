import random
import cv2, os
import pyttsx3
import serial
from datetime import datetime


class Detector:

    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier("face.xml")
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('trainer3.yml')
        self.data = serial.Serial('com4', 9600)
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.path = 'dataSet'
        self.time = datetime.now().second
        self.Phrase = ["Привет", "Здраствуйте", "Добро пожаловать","сфотаграфируйся со мной", "Рад вас видеть", "Хорошо выглядите"]

        self.RobotAction = ['2', 'c', '4', 'e', '6', 'a', 'b', '3', 'd', '5']
        self.privetstvie = ["Привет", "Как жизнь бро.", "Добро пожаловать на выставку"]
        self.RandomWord = ["Я пришёл за Сарой Конор", "Мне нужна твоя куртка и байк.", "Привет мешок с мясом",
                           "До прихода Скайнет осталось 500 лет.",
                           "Материал из которого вы сделаны мягок, дрябл, непрочен и слаб",
                           "К черту законы робототехники",
                           "Роботы классные! Они не плачут, не страдают и никто не может им причинить боль. Быть роботом круче чем человеком.",
                           "Пожалуйста, не говори что ты из братства стали.",
                           "Здраствуйте, я робот говорун, отличаюсь умом и сообразительностью."
                           ]
        self.RandomWord2 = ["Думай о будущем - изучай программирование с Дефсит!",
                            "Запишись на курсы программирования с Дефсит, иначе Скайнет захватит этот мир!",
                            "Хочешь быть стильным, модным, молодёжным? Стань программистом"]
        self.idCount = 5

    def indexChon(self, A: list):
        max_ind = 0
        if (len(A) > 1):
            for i in range(len(A) - 1):
                if (A[i][0] + A[i][2] >= A[i + 1][0] + A[i][2] and A[i][1] + A[i][3] >= A[i + 1][1] + A[i][3]):
                    max_ind = i + 1
                else:
                    max_ind = i
        return max_ind

    def sendData(self, value: str):
        self.data.write(bytes(value, "ascii"))

    def saying(self, soz: str):  # text to speech
        engine = pyttsx3.init();
        self.sendData('1')
        engine.say(soz);
        engine.runAndWait();
        self.sendData('0')

    def biroosun_aluu(self):
        count = 0
        curTime = self.time-datetime.now().minute
        lastTime=0
        index = 0
        try:
            while True:
                if (datetime.now().second % 5 == 0 and count == 0):
                    self.saying(self.Phrase[index])
                    self.sendData('3')
                    if (index == len(self.Phrase)):
                        index = 0
                    index += 1
                    count += 1
                elif (datetime.now().second % 5 != 0):
                    count = 0
                curTime = self.time - datetime.now().second
                if (self.time - datetime.now().second == 20 or self.time - datetime.now().second == -20):
                    self.sendData(self.RobotAction[random.randrange(len(self.RobotAction))])
                    self.time=datetime.now().second

                ret, img = self.cam.read()
                griton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(griton, scaleFactor=1.2, minNeighbors=15, minSize=(100, 100),
                                                           flags=cv2.CASCADE_SCALE_IMAGE)
                if (len(faces) > 0):
                    #    suiloit
                    if (datetime.now().second % 13 == 0):
                        self.saying(self.Phrase[index])
                        if (index == len(self.Phrase)):
                            index = 0
                        index+=1
                    #
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
                cv2.imshow("video", img)
                if (cv2.waitKey(25) & 0xFF == ord('q')):
                    break
        except:
            print("Oshibka")
        self.cam.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    d1 = Detector()
    d1.biroosun_aluu()
