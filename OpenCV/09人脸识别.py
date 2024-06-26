import cv2
import numpy as np
import os
#加载训练数据集文件
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
#准备识别的图片
img=cv2.imread('6.pgm')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier(
    'F:/github/opencv.window/sources/data/haarcascades/haarcascade_frontalface_default.xml')
faces = face_detector.detectMultiScale(gray)
for x, y, w, h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #人脸识别
    id,confidence = recognizer.predict(gray[y:y+h,x:x+w])
    print('id标签：',id,'置信评分：',confidence)
cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
