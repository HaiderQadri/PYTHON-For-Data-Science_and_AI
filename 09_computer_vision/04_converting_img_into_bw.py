# Converting the image into Black and White

# Import the liberaries
import numpy as np
import cv2 as cv

# Read the image
img = cv.imread('09_computer_vision/resources/image.jpg')

# Conversion
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

(thresh, binary) = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

# Show the images
cv.imshow("Original Image", img)
cv.imshow("Gray Image", gray_img)
cv.imshow("Black&White Image", binary)

# Delay code
cv.waitKey(0)
cv.destroyAllWindows()