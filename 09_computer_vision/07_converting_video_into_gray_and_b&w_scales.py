# Converting video into Gray scale and also black and white

# import the liberaries
import numpy as np
import cv2 as cv

# First capture the video
cap = cv.VideoCapture('09_computer_vision/resources/video.mp4')

# Indicator
if (cap.isOpened() == False):
    print("Error in reading video")

while(cap.isOpened()):
    (ret, frame) = cap.read()
    gray_video = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(gray_video, 127, 255, cv.THRESH_BINARY)
    if ret == True:
        cv.imshow("Gray Converted Video", gray_video)
        # cv.imshow("Black and White Video", binary)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
