# Resizing the Image

# Import the liberaries
import numpy as np
import cv2 as cv

# Read the image
img = cv.imread('09_computer_vision/resources/image.jpg')

# Resize the image
res_img = cv.resize(img, (400, 300))

# Show the images
cv.imshow("Original Image", img)
cv.imshow("Resized Image", res_img)

# Delay code
cv.waitKey(0)
cv.destroyAllWindows()