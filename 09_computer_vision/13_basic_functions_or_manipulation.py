<<<<<<< HEAD
# Basic functions or manipulations in openCV

# import the liberaries
import numpy as np
import cv2 as cv

# Read the image 
img = cv.imread('09_computer_vision/resources/image.jpg')

# Resize the image
resized_img = cv.resize(img, (600, 400))

# Convert into Gray Scale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Convert into b&w image
(thresh, binary) = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

# Convert into Blurr
blurr_img = cv.GaussianBlur(img, (25, 25), 0)

# Edge detection
edge_img = cv.Canny(img, 48, 48)

# Thikness of lines
kerel_mat = np.ones((3, 3), np.uint8)
dilated_img = cv.dilate(edge_img, (kerel_mat), iterations=1)

# Make thinner outlines
ero_img = cv.erode(dilated_img, (kerel_mat), iterations=1)

# Crope the image
# First we should know the size of our image
print("The size of the image is:", img.shape)
corpped_img = img[0:400, 0:400]

# Print the images
cv.imshow('Original Image', img)
cv.imshow('Resized Image', resized_img)
cv.imshow('Gray Converted Image', gray_img)
cv.imshow('Black and White Image', binary)
cv.imshow('Blurr Image', blurr_img)
cv.imshow('Edged Image', edge_img)
cv.imshow('Dilated Image', dilated_img)
cv.imshow('Erode Image', ero_img)
cv.imshow('Cropped Image', corpped_img)

cv.waitKey(0)
=======
# Basic functions or manipulations in openCV

# import the liberaries
import numpy as np
import cv2 as cv

# Read the image 
img = cv.imread('09_computer_vision/resources/image.jpg')

# Resize the image
resized_img = cv.resize(img, (600, 400))

# Convert into Gray Scale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Convert into b&w image
(thresh, binary) = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

# Convert into Blurr
blurr_img = cv.GaussianBlur(img, (25, 25), 0)

# Edge detection
edge_img = cv.Canny(img, 48, 48)

# Thikness of lines
kerel_mat = np.ones((3, 3), np.uint8)
dilated_img = cv.dilate(edge_img, (kerel_mat), iterations=1)

# Make thinner outlines
ero_img = cv.erode(dilated_img, (kerel_mat), iterations=1)

# Crope the image
# First we should know the size of our image
print("The size of the image is:", img.shape)
corpped_img = img[0:400, 0:400]

# Print the images
cv.imshow('Original Image', img)
cv.imshow('Resized Image', resized_img)
cv.imshow('Gray Converted Image', gray_img)
cv.imshow('Black and White Image', binary)
cv.imshow('Blurr Image', blurr_img)
cv.imshow('Edged Image', edge_img)
cv.imshow('Dilated Image', dilated_img)
cv.imshow('Erode Image', ero_img)
cv.imshow('Cropped Image', corpped_img)

cv.waitKey(0)
>>>>>>> 115ec8687b96a3320d2901cb6895bf658ababb9f
cv.destroyAllWindows()