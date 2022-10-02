import cv2
import numpy as np

img = cv2.imread('images/OpenCV.jpg')

#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # more colorful

#img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) #less colorful
#img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR) # convert back

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #less colorful
r, g, b = cv2.split(img) # split img on layers
img = cv2.merge([r,g,b]) # get RGB format
img = cv2.merge([b,g,r]) # get BGR format
cv2.imshow("Result", img)
cv2.waitKey(0)