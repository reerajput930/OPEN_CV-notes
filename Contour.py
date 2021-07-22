import cv2 as cv

img = cv.imread("images/riya.jpg")
cv.imshow("img",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)


# observation 
# as we decrease the treshold value more canny can be seen
canny = cv.Canny(img,25,25)
cv.imshow("canny",canny)

# contour is kind of edges(tells how many edges are there)
contours , hiearchies= cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} this is the no of countour')

cv.waitKey(0)