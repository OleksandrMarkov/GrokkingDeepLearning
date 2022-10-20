# importing libraries
import cv2

#import numpy as np
from tkinter import filedialog as fd

filetypes = (
            ('mp4 video files', '*.mp4'),
            ('avi video files', '*.avi')
            )

filename = fd.askopenfilename(
title='Open a video file',
initialdir='C:/Users/ALEX/Documents/grokkingDeepLearning/VisitorsFacesDetection/dataset/videos',
filetypes=filetypes)

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(filename) # 'dataset/videos/Alberto Gilardino-480p.mp4'

# filename.split("/videos/")[1].strip() the video name for the report

 
# Check if camera opened successfully
if (cap.isOpened()== False):
    print(filename.split("/videos/")[1].strip())
    print("Error opening video file")
 
# Read until video is completed
while(cap.isOpened()):
     
# Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
    # Display the resulting frame
        cv2.imshow('Frame', frame)
         
    # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
 
# Break the loop
    else:
        break
 
# When everything done, release
# the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()