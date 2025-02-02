import cv2 as cv

#Reading image

img = cv.imread('./src/test.png')

cv.imshow('Test', img)

#Wait for the user to be close
cv.waitKey(0)