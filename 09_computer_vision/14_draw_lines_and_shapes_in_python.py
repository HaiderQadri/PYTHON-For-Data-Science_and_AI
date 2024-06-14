<<<<<<< HEAD
# How to draw lines and shapes in python

# import the liberaries
import numpy as np
import cv2 as cv

# Draw a convas
# 0 for black images
black_img = np.zeros((600, 600))

# 1 for white image
white_img = np.ones((600, 600))

# Size of the image
print("The size of our image is: ", black_img.shape)

# Color Image
# Let's generate color channel
color_img = np.zeros((600, 600, 3))
# Let's add color
color_img[:] = 255, 0, 179

# Let's color some part of image
color_img[244:400, 100:300] = 255, 0, 0

# Adding line
cv.line(color_img, (0,0), (300, 300), (230, 9, 120), 3)

# Adding another line on the existing line
cv.line(color_img, (100, 100), (400, 400), (255, 255, 10), 3)

# Adding rectangles
cv.rectangle(color_img, (300, 400), (450, 500), (255, 240, 0), 3)

# Filing rectangle 
cv.rectangle(color_img, (300, 400), (450, 500), (255, 240, 0), cv.FILLED)

# Adding circle
cv.circle(color_img, (500, 500), 50, (230, 2, 255), cv.FILLED)

# Display the images
# cv.imshow('Black Image', black_img)
# cv.imshow('White Image', white_img)
cv.imshow("Colored Image", color_img)
cv.waitKey(0)
=======
# How to draw lines and shapes in python

# import the liberaries
import numpy as np
import cv2 as cv

# Draw a convas
# 0 for black images
black_img = np.zeros((600, 600))

# 1 for white image
white_img = np.ones((600, 600))

# Size of the image
print("The size of our image is: ", black_img.shape)

# Color Image
# Let's generate color channel
color_img = np.zeros((600, 600, 3))
# Let's add color
color_img[:] = 255, 0, 179

# Let's color some part of image
color_img[244:400, 100:300] = 255, 0, 0

# Adding line
cv.line(color_img, (0,0), (300, 300), (230, 9, 120), 3)

# Adding another line on the existing line
cv.line(color_img, (100, 100), (400, 400), (255, 255, 10), 3)

# Adding rectangles
cv.rectangle(color_img, (300, 400), (450, 500), (255, 240, 0), 3)

# Filing rectangle 
cv.rectangle(color_img, (300, 400), (450, 500), (255, 240, 0), cv.FILLED)

# Adding circle
cv.circle(color_img, (500, 500), 50, (230, 2, 255), cv.FILLED)

# Display the images
# cv.imshow('Black Image', black_img)
# cv.imshow('White Image', white_img)
cv.imshow("Colored Image", color_img)
cv.waitKey(0)
>>>>>>> 115ec8687b96a3320d2901cb6895bf658ababb9f
cv.destroyAllWindows()