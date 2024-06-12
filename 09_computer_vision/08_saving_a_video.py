# Converting video into gray and saving

# import the liberaries
import numpy as np
import cv2 as cv

# Capture the video
cap = cv.VideoCapture('09_computer_vision/resources/video.mp4')

# Writingformat, codec, video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('09_computer_vision/resources/converted_video.avi', cv.VideoWriter_fourcc('M', 'j', 'P', 'G'), 10, (frame_width, frame_height), isColor = False)

# Indicator
if (cap.isOpened() == False):
    print("Error in reading video")

while(cap.isOpened()):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if ret == True:
        out.write(grayframe)
        cv.imshow("Gray Converted Video", grayframe)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()
