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