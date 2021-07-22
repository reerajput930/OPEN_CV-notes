import cv2 as cv

def Rescale(frame, scale = 0.20):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimenstion= (width,height)
 
    return  cv.resize(frame,dimenstion,interpolation=cv.INTER_AREA)



# capture the video
capture = cv.VideoCapture("images/riya_video.mp4")

while True:
    #taking each frame
    isTrue,frame = capture.read()
    # showing each frame
    resize_frame = Rescale(frame)
    # cv.imshow('Video',frame)
    cv.imshow('Video Resized',resize_frame)

    # waitkey means how wait needed to another frame
    # 0xff == ord() pressing the key to quit
    if cv.waitKey(2) & 0xFF == ord('d'):
        break


# relase the capture
capture.release()
# destroy the all window open
cv.destroyAllWindows()