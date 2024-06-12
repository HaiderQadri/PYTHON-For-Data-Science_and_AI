# How to capture webcam in python

# import the liberaries
import numpy as np
import cv2 as cv

# Capture the webcam
cap = cv.VideoCapture(0) # 1 webcam

while(cap.isOpened()):
    # Capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        # Show the frames
        cv.imshow('Webcam', frame)
        # q for quit
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break    

cap.release()
cv.destroyAllWindows()