import cv2 as cv
import numpy as ny

img = cv.imread("images/riya.jpg")
cv.imshow("pic",img)


# resizing
resize = cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resize",resize)

#flipping
# three types of flip code 
# 1 = flip in horizontaly
# 0 = flip in verticaly
# -1 = both horizontaly and verticaly
flip = cv.flip(img,-1)
cv.imshow("flip",flip)

# croping    
# (x1,y1) (x2,y2)
croping  = img[200:300,300:400]
cv.imshow("croping",croping)


# you can also translate and rotate check out it net(we have to make function for that)

cv.waitKey(0)