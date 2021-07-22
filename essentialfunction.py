import cv2 as cv

img = cv.imread('images/riya.jpg')
cv.imshow('riya',img)

# coverting to gray scal
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)


# BLUR
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

# edge detect
canny = cv.Canny(img,125,175)
# cv.imshow('canny',canny)

# resized
resized = cv.resize(img,(700,600),interpolation=cv.INTER_AREA)
cv.imshow("re",resized)

cv.waitKey(0)