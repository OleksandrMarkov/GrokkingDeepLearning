import os, shutil

from package.constants import *

from tkinter import filedialog

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

	import subprocess # для виявлення флешки
	def get_path_to_new_collection(self):
		path = None
		out = subprocess.check_output(DISKS_CAPTIONS, shell = True)
		for drive in str(out).strip().split('\\r\\r\\n'):
			if '2' in drive:
				drive_letter = drive.split(':')[0]
				if drive_letter not in PC_DISKS:
					path = 	f"{drive_letter}:/{IMAGES_FOLDER_ON_USB_FLASH_DRIVE}"
					break
		return path

	def get_new_collection(self, path):
		return os.listdir(path)	
		
	def move_images(self, collection, path):
		for img in collection:
			if img.endswith(IMAGE_ENDS_WITH):
				copyfile(f"{path}/{n}", f"{PHOTOS_FOLDER}/{n}")	