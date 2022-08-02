
import cv2 
import numpy as np 

detector=cv2.CascadeClassifier("C:/Users/hi/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
cam =cv2.VideoCapture("F:/dataaa/ahmed ashref.mp4") 
Id=input('enter your id: ') 
#Username=input('Enter User Name : ') 
sampleNum=0 
while (True): 
    ret,img=cam.read() 
    #gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    faces=detector.detectMultiScale(img,1.3,5) 
    for(x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 
        sampleNum=sampleNum+1 
        cv2.imwrite("F:/VGG/train/ahmed ashref/"+Id+'.'+str(sampleNum)+".jpg",img[y:y+h,x:x+w]) 
        cv2.imshow('frame',img) 
 
    if cv2.waitKey(100 ) &0xFF ==ord('q'): 
        break 
    elif sampleNum>150: 
        break 
         
cam.release() 
cv2.destroyAllWindows()