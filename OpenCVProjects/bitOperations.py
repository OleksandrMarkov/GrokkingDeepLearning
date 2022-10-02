import cv2
import numpy as np

photo = cv2.imread('images/OpenCV.jpg')
img = np.zeros(photo.shape[:2], dtype = 'uint8')

#img = np.zeros((350, 350), dtype = 'uint8')

circle = cv2.circle(img.copy(), (200,300), 120, 255, -1) # white circle r = 120
square = cv2.rectangle(img.copy(), (25, 25), (350,350), 255, -1)

#img = cv2.bitwise_and(circle, square) # AND
#img = cv2.bitwise_or(circle, square) # OR
#img = cv2.bitwise_xor(circle, square) # XOR
#img = cv2.bitwise_not(circle) # NOT

img = cv2.bitwise_and(photo, photo, mask = circle) # get a round part of img

cv2.imshow("Result", img)
cv2.waitKey(0)