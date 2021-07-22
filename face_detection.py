# we are doing face detection 
# we also copied the haar cascades face detector in xml file which is free for user use from github
# Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data.
#  OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc..
import cv2 as cv

# reading the images
img1 = cv.imread("images/riya.jpg")
img2 = cv.imread("images/friends.jpg")
img3 = cv.imread("images/TwoFriends.jpg")


# changing it to grayscale, reason: beacuse in face detection ,color in picture not needed
gray1 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
gray3 = cv.cvtColor(img3,cv.COLOR_BGR2GRAY)

# loading the data of cascade
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# detectin the face, detection happen in rectangular form
# detectMultiScale(image, scale , noice detecter(senstive to edges lines))
face1 = face_cascade.detectMultiScale(gray1,1.1,4)
face2 = face_cascade.detectMultiScale(gray2,1.1,4)
face3 = face_cascade.detectMultiScale(gray3,1.1,3)


# marking the detected part
for (x,y,w,h) in face1:
    cv.rectangle(img1,(x,y),(x+w,y+h),(0,250,0),3)


for (x,y,w,h) in face2:
    cv.rectangle(img2,(x,y),(x+w,y+h),(0,250,0),3)

for (x,y,w,h) in face3:
    cv.rectangle(img3,(x,y),(x+w,y+h),(0,250,0),3)


cv.imshow("image1",img1)
cv.imshow("image2",img2)
cv.imshow("image3",img3)

cv.waitKey(0)