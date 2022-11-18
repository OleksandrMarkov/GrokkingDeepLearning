import os, shutil
from shutil import copyfile, ignore_patterns
from package.constants import *
from tkinter import filedialog
from package.classes.Image import *

import subprocess # для виявлення флешки

class Helper:
	def remove_old_snapshots(self, snapshots_folder):
		for files in os.listdir(snapshots_folder):
			full_path = os.path.join(snapshots_folder, files)
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
			#print(f"{path}/{img}")
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
						#print('cant crop')
						print(e)