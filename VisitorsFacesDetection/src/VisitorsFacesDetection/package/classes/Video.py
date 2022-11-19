import cv2, os, time

import face_recognition  #pip install dlib & pip install face-recognition
from package.constants import *


class Video:
	#def __init__(self, path, image_encodings):
	def __init__(self, path):
		self.path = path[path.find(VIDEOS_FOLDER + "/"):]
		print(self.path)

		#self.path = path.split(f"{VIDEOS_FOLDER}/")[1]
		
		self.cap = cv2.VideoCapture(path)
		
		#self.cap = cv2.VideoCapture("dataset/videos/2.mp4")
		self.face_cascade = cv2.CascadeClassifier(FACE_RECOG_MODEL)
		

	def get_face_locations(self, frame):
		return face_recognition.face_locations(frame)

	def get_face_encodings(self, frame, locations):
		return face_recognition.face_encodings(frame, locations)		

	def catch_matches(self, image_encodings):
		print("Trying to catch...")
		while self.cap.read():
			try:
				success, img = self.cap.read()
				frame = img[:, :, ::-1]

				face_locations = self.get_face_locations(frame)
				face_encodings = self.get_face_encodings(frame, face_locations)

				for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
					matches = face_recognition.compare_faces(image_encodings, face_encoding)
					if True in matches:
						cv2.imwrite(os.path.join(SNAPSHOTS, "Recognized visitor " + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
						print("Abuser is detected!")
						return True
					else:
						print("...")
			except Exception as e:
				print("Catch error")
				print(e)			
		return False