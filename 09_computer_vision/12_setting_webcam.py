<<<<<<< HEAD
# Setting of webcam or video

# import the liberaries
import numpy as np
import cv2 as cv

# Capture the webcam
cap = cv.VideoCapture(0) # 1 webcam

cap.set(10, 100) # 10 is the key for brightness
cap.set(3, 640) # 3 is the key for width
cap.set(4, 480) # 4 is the key for height

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
=======
# Setting of webcam or video

# import the liberaries
import numpy as np
import cv2 as cv

# Capture the webcam
cap = cv.VideoCapture(0) # 1 webcam

cap.set(10, 100) # 10 is the key for brightness
cap.set(3, 640) # 3 is the key for width
cap.set(4, 480) # 4 is the key for height

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
>>>>>>> 115ec8687b96a3320d2901cb6895bf658ababb9f
cv.destroyAllWindows()