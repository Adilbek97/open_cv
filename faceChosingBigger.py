import numpy as np
import cv2

detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
def listChon(A:list):
    max_ind=0
    for i in range(len(A)-1):
      if(A[i][0]+A[i][2]>=A[i+1][0]+A[i][2] and A[i][1]+A[i][3]>=A[i+1][1]+A[i][3]):
          max_ind=i+1
      else:
          max_ind=i
    return max_ind
        
        
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    #for (x,y,w,h) in faces:
    length=len(faces)
    print(length)
    if(length>1):
        max_index=listChon(faces)
        for i in range(length):
            if(i==max_index):
                continue
            cv2.rectangle(img,(faces[i][0],faces[i][1]),(faces[i][0]+faces[i][2],faces[i][1]+faces[i][3]),(255,0,0),2)
        cv2.rectangle(img,(faces[max_index][0],faces[max_index][1]),(faces[max_index][0]+faces[max_index][2],faces[max_index][1]+faces[max_index][3]),(0,0,255),2)
    elif(length<2 and length>0 ):
     cv2.rectangle(img,(faces[0][0],faces[0][1]),(faces[0][0]+faces[0][2],faces[0][1]+faces[0][3]),(255,0,0),2)
     print("x= ",faces[0])
    #print("y= ",y)
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
