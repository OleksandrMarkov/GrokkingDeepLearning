""" https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py """
# 1) crop all images
# 2) convert them (COLOR_BGR2GRAY)
# 3) create array of encodings
# 4) comparing while reading frames, if matches then break and send message to telegram

import cv2
import face_recognition
import os

cap = cv2.VideoCapture("dataset/videos/2.mp4")


#tmp = cv2.imread("dataset/photos/2.png")
#gray = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
#cv2.imwrite("dataset/photos/2GRAYGRAYGRAY.png", gray)
#print("!!!")


image_to_recognition = face_recognition.load_image_file("dataset/photos/2GRAYGRAYGRAY.png")



image_enc = face_recognition.face_encodings(image_to_recognition)[0]

image_encs = [image_enc]


recognizer_cc = cv2.CascadeClassifier('model/faces.xml')


while cap.read(): # True 
	success,img = cap.read()
	rgb_frame = img[:, :, ::-1]

	face_locations = face_recognition.face_locations(rgb_frame)
	face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

	for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
		matches = face_recognition.compare_faces(image_encs, face_encoding)
		if True in matches:
			print("Abuser is detected!")
		else:
			print("...")	

print("!!!")			