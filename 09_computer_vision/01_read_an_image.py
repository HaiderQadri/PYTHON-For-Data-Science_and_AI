# Read an image and display that image

# import the liberarie
import numpy as np
import cv2 as cv

# Read the image
img = cv.imread('09_computer_vision/resources/image.jpg')

# Show the image
cv.imshow('First Image', img)

# For Delay in image 
cv.waitKey(0) # 0 Means forever
cv.destroyAllWindows()

# Press q for quit the image