import cv2 as cv
img = cv.imread('lena.jpg')
cv.imshow('img', img)
print('原来图片的尺寸', img.shape)
resize_img = cv.resize(img,dsize=(200, 240))
print('修改后图片的尺寸', resize_img.shape)
cv.imshow('resize_img', resize_img)

#只有输入q的时候才退出
# cv.waitKey(0)
while True:
    if ord('q') == cv.waitKey(0):
        break
    # code = cv.waitKey()
    # print(code)
cv.destroyWindow()