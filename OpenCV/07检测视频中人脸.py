import cv2 as cv
def face_detect_demo(img):
    #将图片灰度
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier(
        'F:/github/opencv.window/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(gray)
    for x,y,w,h in faces:
        # cv.rectangle(img,(x,y),(x+y, y+h), color=(0,0,255), thickness=2)
        cv.circle(img,center = (x+w//2,y+h//2), radius = w//2, color= (0,0,255), thickness = 2)
    cv.imshow('result',img)
#读取视频
cap = cv.VideoCapture('video.mp4')
while True:
    flag,frame = cap.read()
    print('flag:',flag,'frame.shape:',frame.shape)
    if not flag:
        break
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(10):
        break
cv.destroyAllWindows()
cap.release()