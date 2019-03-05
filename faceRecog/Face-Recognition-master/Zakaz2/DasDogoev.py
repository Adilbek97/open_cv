import pyttsx3
import serial

def saying(soz: str,data):  # text to speech

    engine = pyttsx3.init();
    data.write(bytes('1', "ascii"))
    engine.say(soz);
    engine.runAndWait();
    data.write(bytes('0', "ascii"))

if __name__=="__main__":
    data = serial.Serial('com4', 9600)
    i = int(input("0 du jaz..."))
    if(i==0):
        # saying("Здравствуйте, Дастан Давлетович. Я рад приветствовать вас на конференции 'Информационные технологии в госсекторе'.",data)
        # saying("Спутник Кыргызстан. Говорим то, о чем другие молчат.", data)
        saying("Айнура с днем рождения", data)
    if(i==1):
        data.write(bytes('s', "ascii"))
    if(i == 2):
        data.write(bytes('e', "ascii"))
