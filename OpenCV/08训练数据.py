# import os
# import cv2
# import sys
# from PIL import Image
# import numpy as np
# def getImageAndLabels(path):
#     facesSamples = []
#     ids = []
#     # imagePath=[os.path.join(path.f) for f in os.listdir(path)]
#     imagePath = [os.path.join(path, f) for f in os.listdir(path)]
#     #检测人脸
#     face_detector = cv2.CascadeClassifier(
#         'F:/github/opencv.window/sources/data/haarcascades/haarcascade_frontalface_default.xml')
#
#     # print(imagePaths)
#     #遍历列表中的图片
#     for imagePath in imagePath:
#         #打开图片
#         PIL_img=Image.open(imagePath).convert('L')
#         #将图像转换为数组
#         img_numpy=np.array(PIL_img,'uint8')
#         faces = face_detector.detectMultiScale(img_numpy)
#         #获取每张图片的id
#         print(os.path.split(imagePath))
#         # int(os.path.split(imagePath)[1].split(',')[0])
#         int(os.path.split(imagePath)[1].split('.')[0])
#         for x,y,w,h in faces:
#             facesSamples.append(img_numpy[y:y+h,x:x+h])
#             ids.append(id)
#     return facesSamples.ids
#
# if __name__ == '__main__':
#     #图片路径
#     path = './data/jm/'
#     #获取图像数组和id标签数组
#     faces,ids=getImageAndLabels(path)
#     #获取循环对象
#     recognizer = cv2.face.LBPHFaceReconizer_creat()
#     recognizer.train(faces,np.array(ids))
#     #保存文件
#     recognizer.write('trainer/trainer.yml')

import os
import cv2
from PIL import Image
import numpy as np


def getImageAndLabels(path):
    facesSamples = []
    ids = []
    imagePath = [os.path.join(path, f) for f in os.listdir(path)]

    face_detector = cv2.CascadeClassifier(
        'F:/github/opencv.window/sources/data/haarcascades/haarcascade_frontalface_default.xml')

    for imagePath in imagePath:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')
        faces = face_detector.detectMultiScale(img_numpy)

        id = int(os.path.split(imagePath)[1].split('.')[0])

        for x, y, w, h in faces:
            facesSamples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)

    return facesSamples, ids


if __name__ == '__main__':
    path = './data/jm/'
    faces, ids = getImageAndLabels(path)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(ids))

    recognizer.write('trainer/trainer.yml')