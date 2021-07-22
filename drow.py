import cv2 as cv
import numpy as np


# in order to create the blank image use numpy liberary
# np.zeros((height,width,channal),datatype)
blank = np.zeros((500,600,3),dtype='uint8')
# cv.imshow('Blank',blank)


# drawing the rectangle use cv.rectangle
# cv.rectangle(img,starting(dis-y,dis-x),bottom(dis-y,dis-x),(b,g,r),thivkness(-1 means fillup))
cv.rectangle(blank,(0,0),(350,250),(0,255,0),thickness=-1)
# cv.imshow("Blank_rec",blank)


# circle
# cv.circle(img,(dis-y,dis-x),radius,(b,g,r),thivkness(-1 means fillup))
cv.circle(blank,(350,250),70,(0,0,250),thickness=-1)
# cv.imshow("Blank_circle",blank)

# line
# cv.line(img,starting(x-axis,y-axis),(x-axis,y-axis),(b,g,r),thivkness(-1 means fillup))
cv.line(blank,(0,0),(350,250),(250,0,0),thickness=1)
# cv.imshow("Blank_line",blank)

# text
cv.putText(blank,'hello',(350,220),cv.FONT_HERSHEY_TRIPLEX,2,(250,250,250),3)
cv.imshow("blank_text",blank)

cv.waitKey(0)



