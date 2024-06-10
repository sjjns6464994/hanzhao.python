import cv2 as cv
img = cv.imread('lena.jpg')
#左上角的坐标是（x,y）矩形的宽度和高度
x,y,w,h = 100, 100, 100, 100
cv.rectangle(img,(x,y,x+w,y+h),color=(0,0,255),thickness=2)
#绘制圆center元组指圆点的坐标
# x,y,r = 200,200,100
# cv.circle(img, center=(), radius=, color=(0,0,255), thickness=2)
#显示图片
cv.imshow('rectangle_img',img)
cv.waitKey(0)
cv.destroyWindow()