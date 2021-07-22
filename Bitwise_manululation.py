import cv2 as cv
import numpy as ny

# there are three type of bitwise
# and or xor

blank = ny.zeros((500,600),dtype='uint8')
cv.imshow("blank img",blank)

rectangle = cv.rectangle(blank.copy(),(50,40),(550,450),225,-1)
cv.imshow("rectangle",rectangle)
circle = cv.circle(blank.copy(),(300,250),200,900,-1)
cv.imshow("circle",circle)

# bitwise_and --- give intersection part
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("bitwise_and",bitwise_and)
# bitwise_or --- give intersection and non intersection part
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("bitwise_or",bitwise_or)
# bitwise_xor-- give only non-interaction part
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("bitwise_XOR",bitwise_xor)


cv.waitKey(0)