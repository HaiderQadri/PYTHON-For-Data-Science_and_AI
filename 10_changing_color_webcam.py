# Changing webcam to gray and lack and white

# import the liberaries
import numpy as np
import cv2 as cv

# Capture the webcam
cap = cv.VideoCapture(0) # 1st webcam

while(cap.isOpened()):
    ret, frame = cap.read()
    # Converting into gray scale
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Converting into black and white scale
    (thresh, binary) = cv.threshold(gray_frame, 127, 255, cv.THRESH_BINARY)

    # Show the cams
    cv.imshow("OriginalCam", frame)
    cv.imshow("GrayCam", gray_frame)
    cv.imshow("Black and White Cam", binary)

    # q for quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()