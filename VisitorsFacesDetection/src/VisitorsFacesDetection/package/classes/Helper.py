import os, shutil
from shutil import copyfile, ignore_patterns
from package.constants import *
from tkinter import filedialog
from package.classes.Alerts import *
from package.classes.Image import *
from package.classes.ProcessedImage import *

import subprocess # для виявлення флешки
import time

class Helper:
	def remove_old_snapshots(self):
		for files in os.listdir(SNAPSHOTS):
			full_path = os.path.join(SNAPSHOTS, files)
			try:
				shutil.rmtree(full_path)
			except OSError:
				os.remove(full_path)

	def remove_old_processed_photos(self):
		for files in os.listdir(PROCESSED_PHOTOS_FOLDER):
			full_path = os.path.join(PROCESSED_PHOTOS_FOLDER, files)
			try:
				shutil.rmtree(full_path)
			except OSError:
				os.remove(full_path)		

	def get_videofile(self):
		return filedialog.askopenfilename(title = SELECT_VIDEO,
			initialdir = VIDEOS_FOLDER,
			filetypes = VIDEOTYPES)

	def get_path_to_new_collection(self):
		path = None
		out = subprocess.check_output(DISKS_CAPTIONS, shell = True)
		for drive in str(out).strip().split('\\r\\r\\n'):
			if '2' in drive:
				drive_letter = drive.split(':')[0]
				if drive_letter not in PC_DISKS:
					path = 	f"{drive_letter}:/{IMAGES_FOLDER_ON_USB_FLASH_DRIVE}"
					break
		#print(path) # F:/photos 			
		return path
		
	def move_images(self, path):
		print(path)
		collection = os.listdir(path)
		for img in collection:
			if img.endswith(('jpg', 'png', 'gif')):
				copyfile(f"{path}/{img}", f"{FULL_PATH_TO_PHOTOS_FOLDER}/{img}")


	def crop_images_from_the_collection(self):
		for (root, dirs, images) in os.walk(PHOTOS_FOLDER):
			for image_name in images:
				if (".jpg" in image_name or ".png" in image_name or ".gif" in image_name) and (PROCESSED_PHOTOS_FOLDER not in os.path.join(root, image_name).replace("\\", "/")):
					try:	
						path = os.path.join(root, image_name).replace("\\", "/")
						#print(path) # dataset/photos/michael_jackson/Agosto_01918_2.png
						
						img = Image(path)
						#img.test()
						img.crop_face()
							
					except Exception as e:
						pass

	def iterate_processed_images(self, video):
		images_dict = {}			
		for (root, dirs, images) in os.walk(PROCESSED_PHOTOS_FOLDER):
			for image_name in images:
				# dataset/photos/processed photos/will_smith.png
				
				path = os.path.join(root, image_name).replace("\\", "/")
				#print(path)
				
				image = ProcessedImage(path)
				image_encodings = image.get_encodings()

				images_dict[image] = image_encodings

				#if image_encodings is not None:
				#	print(path)
				#if video.catch_matches(image_encodings) == True:
						#print(image_name)
						#self.add_person_to_report()
		
		print(len(images_dict))				
		print("All faces are checked!")

		#video.capture_matches(images_dict)
		captured_visitors = video.capture_matches(images_dict)
		snapshots_amount = self.get_amount_of_snapshots()

		report = Report(captured_visitors, snapshots_amount)
		#if self.no_visitors(captured_visitors) == True:
		#	self.info = Info()
		#	self.info.show(message = NO_VISITORS)
		#else:
		#	for visitor in captured_visitors:
		#		print(visitor.path)

	def get_amount_of_snapshots(self):
		return len([entry for entry in os.listdir(SNAPSHOTS)\
		 if os.path.isfile(os.path.join(SNAPSHOTS, entry))])
				

	def no_visitors(self, visitors):
		if len(visitors) == 0:
			return True
		return False	
		
	def add_person_to_report(self):
		pass

	def send_report(self):
		pass				