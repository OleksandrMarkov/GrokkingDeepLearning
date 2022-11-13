import os, shutil

class Helper:
	def remove_old_snapshots(self, snapshots_folder):
		for files in os.listdir(snapshots_folder):
			full_path = os.path.join(snapshots_folder, files)
			try:
				shutil.rmtree(full_path)
			except OSError:
				os.remove(full_path)