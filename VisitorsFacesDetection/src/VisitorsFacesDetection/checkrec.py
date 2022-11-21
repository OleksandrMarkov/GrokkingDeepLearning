""" https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py """

# 1) crop all images
# 2) convert them (COLOR_BGR2GRAY)
# 3) create array of encodings
# 4) comparing while reading frames, if matches then break and send message to telegram

import cv2
import face_recognition
import os

cap = cv2.VideoCapture("dataset/videos/2.mp4")

image1 = face_recognition.load_image_file("dataset/photos/processed photos/Danil_Alifovich_1.png")
image2 = face_recognition.load_image_file("dataset/photos/processed photos/stephen McDaniel_3.jpg")
image3 = face_recognition.load_image_file("dataset/photos/processed photos/gilardino.png")


image_enc1 = face_recognition.face_encodings(image1)[0]
image_enc2 = face_recognition.face_encodings(image2)[0]
image_enc3 = face_recognition.face_encodings(image3)[0]

image_encs1 = [image_enc1]
image_encs2 = [image_enc2]
image_encs3 = [image_enc3]

image_encs_arr = [image_encs1, image_encs2, image_encs3]

recognizer_cc = cv2.CascadeClassifier('model/faces.xml')

results = []

while cap.read(): # True 
	success,img = cap.read()

	if not success:
		break

	rgb_frame = img[:, :, ::-1]

	face_locations = face_recognition.face_locations(rgb_frame)
	face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

	for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
					
		matches1 = face_recognition.compare_faces(image_encs1, face_encoding)
		matches2 = face_recognition.compare_faces(image_encs2, face_encoding)
		matches3 = face_recognition.compare_faces(image_encs3, face_encoding)
		
		if True in matches1:
			#print("Abuser is detected!")
			print(1)
		elif True in matches2:
			print(2)
		elif True in matches3:
			print(3)
		else:
			print("...")	

print("!!!")
