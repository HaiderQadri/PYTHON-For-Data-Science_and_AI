# How to read a video file using computer vision

# import the liberary
import numpy as np
import cv2 as cv

# Capture the video
cap = cv.VideoCapture('09_computer_vision/resources/video.mp4')

# Indicator
if (cap.isOpened() == False):
    print("Error in reading video")

# Reading and playing video

while(cap.isOpened()):
    (ret, frame) = cap.read()
    if ret == True:
        cv.imshow('Video', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()    