import cv2


def add(cam):
    detector = cv2.CascadeClassifier('Classifiers/face.xml')
    i = 0
    offset = 50
    name = input('enter your id')
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100))
        for (x, y, w, h) in faces:
            i = i + 1
            cv2.imwrite("dataSet/face-" + name + '.' + str(i) + ".jpg",
                        gray[y - offset:y + h + offset, x - offset:x + w + offset])
            cv2.rectangle(im, (x - 50, y - 50), (x + w + 50, y + h + 50), (225, 0, 0), 2)
            cv2.imshow('im', im)
            cv2.waitKey(100)
        if i > 20:
            cam.release()
            cv2.destroyAllWindows()
            break

