import pyttsx3
import random
import serial
# data = serial.Serial('com4',9600)
def saying(soz: str,data):  # text to speech
    engine = pyttsx3.init();
    data.write(bytes('1', "ascii"))
    engine.say(soz);
    engine.runAndWait();
    data.write(bytes('0', "ascii"))


if __name__=="__main__":
    while True:
    # data = serial.Serial('com4', 9600)
        i = random.randrange(15)
        print(i)
    # if(i==0):
    # ""Здравствуйте! Добро пожаловать на конференцию 'Информационные технологии в госсекторе'.",
    #                    "Здравствуйте! Компания Гринлайн  приветствует вас на конференции IT in Government 2018.",
    #
    # #     saying("Спутник Кыргызстан. Говорим то, о чем другие молчат.",data)