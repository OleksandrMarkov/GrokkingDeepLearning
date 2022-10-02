import cv2
import numpy as np

# matrix of zeros - absolutely black img
# matrix of ones - absolutely white img

# BGR is standard in openCV (reversed RGB): blue, green, red
photo = np.zeros((450,450, 3), dtype = 'uint8') # 3 layers

#photo[:] = 255, 0, 0 # absolutely blue
#photo[100:150, 200:280] = 255, 0, 0 # paint over 100:150 (height) and 200:280 (width)

cv2.rectangle(photo, (50,70) , (100,100), (255,0,0), thickness = cv2.FILLED) # rectangle frame
# img
# start point: X,Y
# end point: X,Y
# color
# thickness = cv2.FILLED (filling) / 1 (not filled)


cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (255,0,0), thickness = 3) # line
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (255,0,0), thickness = cv2.FILLED) # circle radius = 50

cv2.putText(photo, 'Some text', (100, 150), cv2.FONT_ITALIC, 1, (150,150,150), thickness =1)

cv2.imshow('Photo', photo)
cv2.waitKey(0)