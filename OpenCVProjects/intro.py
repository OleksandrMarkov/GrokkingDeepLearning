import cv2
import numpy as np

# PICTURES 
img = cv2.imread('images/OpenCV.jpg')
img = cv2.resize(img,(img.shape[1] * 2, img.shape[0] * 2))

#img = cv2.GaussianBlur(img, (9,9), 0) # 9,9 - only odd numbers for blur(1,3,5,7, ...) размытие

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 200, 200) # black-white только контуры: img в бинарном формате. чем мешьше значение тем больше точность

kernel = np.ones((5,5), np.uint8) # matrix 5x5

img = cv2.dilate(img, kernel, iterations=1)

img = cv2.erode(img, kernel, iterations=1)
cv2.imshow('Result', img)
# img[0:100, 0:150] crop an image

print(img.shape) # colors layers

cv2.waitKey(0)

# VIDEOS

#cap = cv2.VideoCapture('videos/road.mp4') # 0 - first web-camera
#cap.set(3, 500) # id of width = 3
#cap.set(4, 300) # id of height = 3

#while True:
#    success, img = cap.read() # success - True/False
#    cv2.imshow('Result', img)   
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
        