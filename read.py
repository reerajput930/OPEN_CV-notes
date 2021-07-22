# importing the cv
import cv2 as cv

# # this is to read the image
# image = cv.imread("images/riya.jpg") 

# # this is to show the image
# cv.imshow('person',image)
# # this is to wait till we don't press any key
# cv.waitKey(0)


# capture the video
capture = cv.VideoCapture("images/riya_video.mp4")

while True:
    #taking each frame
    isTrue,frame = capture.read()
    # showing each frame
    cv.imshow('Video',frame)

    # waitkey means how wait needed to another frame
    # 0xff == ord() pressing the key to quit
    if cv.waitKey(2) & 0xFF == ord('d'):
        break


# relase the capture
capture.release()
# destroy the all window open
cv.destroyAllWindows()