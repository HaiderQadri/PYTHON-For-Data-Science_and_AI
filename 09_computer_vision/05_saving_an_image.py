# Saving an Image

# Import the liberaries
import numpy as np
import cv2 as cv

# Read the image
img = cv.imread('09_computer_vision/resources/image.jpg')

# Conversion
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

(thresh, binary) = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

# Saving the Image
cv.imwrite( "09_computer_vision/resources/gray_image.jpg", gray_img)
cv.imwrite( '09_computer_vision/resources/black_and_white_image.jpg', binary)

# # Show the images
# cv.imshow("Original Image", img)
# cv.imshow("Gray Image", gray_img)
# cv.imshow("Black&White Image", binary)

# # Delay code
# cv.waitKey(0)
# cv.destroyAllWindows()