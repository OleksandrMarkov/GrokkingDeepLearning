import cv2

import face_recognition  #pip install dlib & pip install face-recognition
from package.constants import *

from package.classes.Image import *
from package.classes.Video import *

class ProcessedImage(Image):
	def __init__(self, path):
		
		self.path = path
		print(self.path)
		
		self.img = cv2.imread(path)
		

		#self.path = path.split(f"{PROCESSED_PHOTOS_FOLDER}/")[1] # name like 1.png
		#self.face_cascade = cv2.CascadeClassifier(FACE_RECOG_MODEL)

	def test(self):
		pass
		
	#def show_image(self):
	#	cv2.imshow("test", self.img)

	def get_faces(self):
		gray = self.convert2Gray()
		faces = self.face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)
		return faces

	def get_encodings(self):
		
		#image = face_recognition.load_image_file(self.path)
		#image = self.img
		try:
			image_enc = face_recognition.face_encodings(image)[0]
			image_encs = [image_enc]
			return image_encs
		except Exception as e:
			print("Encodings error")
			print(e)
				