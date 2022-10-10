import cv2
import face_recognition
import os

cap = cv2.VideoCapture(0)
# 0 web-камера
# or set path to video.mp4

image_to_recognition = face_recognition.load_image_file('images/to_recog/practice/0.jpg')     

image_enc = face_recognition.face_encodings(image_to_recognition)[0]

recognizer_cc = cv2.CascadeClassifier('faces.xml')

while True:
	success, img = cap.read()
	recognize = recognizer_cc.detectMultiScale(img, scaleFactor=2, minNeighbors=3)

	if len(recognize) != 0:
		print("Found!!!")
		unknown_face = face_recognition.face_encodings(img) # face from video frame
		
		# compare unknown with abuser 	    
		compare = face_recognition.compare_faces([unknown_face], image_enc)
  
		if compare == True:
			print('Web camera fixed abuser.')
		else:
			pass