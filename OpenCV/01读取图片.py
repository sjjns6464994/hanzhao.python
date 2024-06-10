import cv2 as cv
#读取图片
img = cv.imread('lena.jpg')
#显示图片
cv.imshow('read_img', img)
#等待键盘输入 单位毫秒传入0则是无限等待
cv.waitKey(0)
#释放内存  OpenCV底层是c++写的
cv.destroyWindow()