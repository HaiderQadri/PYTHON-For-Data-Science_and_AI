# Resizing the ImageConverting the image into Gray Scale

# Import the liberaries
import numpy as np
import cv2 as cv

# Read the image
img = cv.imread('09_computer_vision/resources/image.jpg')

# Conversion
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Show the images
cv.imshow("Original Image", img)
cv.imshow("Converted Image", gray_img)

# Delay code
cv.waitKey(0)
cv.destroyAllWindows()