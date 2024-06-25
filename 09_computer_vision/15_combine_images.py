# How to combine images

# import necessary liberaries
import numpy as np
import cv2 as cv

# Load the image 
img_1 = cv.imread('09_computer_vision/resources/image.jpg')
img_2 = cv.imread('09_computer_vision/resources/gray_image.jpg')

# Stacking same image

# 1. Horizontal stack
hor_img = np.hstack((img_1, img_1))

# 2. Vertical stack
ver_img = np.vstack((img_2, img_2))

# Show the image
cv.imshow('Horizontal Stacked Images', hor_img)
cv.imshow('Vertical Stacked Images', ver_img)

cv.waitKey(0)
cv.destroyAllWindows()