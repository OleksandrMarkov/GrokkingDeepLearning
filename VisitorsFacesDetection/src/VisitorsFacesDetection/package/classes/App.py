from tkinter import *
from tkinter import messagebox

from package.constants import *

from tkinter import filedialog

from shutil import copyfile, ignore_patterns

#from Helper import *
#import Helper
from package.classes.Helper import *

import PIL.Image, PIL.ImageTk
import cv2

import face_recognition  #pip install dlib & pip install face-recognition 

import os, shutil

import subprocess # для виявлення флешки
import time

class App():
	def __init__(self, window):

		self.helper = Helper()
		self.window = window
		self.window.title(WINDOW_TITLE)

		self.window.iconbitmap(ICON)
		self.window.resizable(False, False)

		self.launch = False 
		self.selected_video = None 

		# Блок для обраного відео
		top_frame = Frame(self.window)
		#top_frame.pack_propagate(False)

		top_frame.pack(side = TOP, pady = 10)

		# Блок для кнопок
		btn_frame = Frame(self.window, bg = BTN_FRAME_COLOR)
		btn_frame.pack(side = BOTTOM, pady = 5)

		self.pause = False   # Керування кнопкою "Пауза"

		self.canvas = Canvas(top_frame)
		self.canvas.pack()

		# Кнопка "Відеозапис"
		self.btn_select_video = Button(btn_frame, text = SELECT_VIDEO, width = BTN_W, command = self.open_video)
		self.btn_select_video.grid(row = 0, column = 0, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		# Кнопка "Розпізнавання"
		self.btn_recognize_faces = Button(btn_frame, text = START_RECOGNITION, width = BTN_W, command = self.recognize_faces)
		self.btn_recognize_faces.grid(row = 0, column = 1, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		# Кнопка "Оновити колекцію зображень"
		self.btn_update_photo_collection = Button(btn_frame, text = NEW_IMGS, width = BTN_W, command = self.update_photo_collection)
		self.btn_update_photo_collection.grid(row = 0, column = 2, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		# Кнопка "Довідка"
		self.btn_open_FAQ = Button(btn_frame, text = FAQ, width = BTN_W)
		self.btn_open_FAQ.grid(row = 0, column = 3, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		# Кнопка "Запуск"
		self.btn_launch_video = Button(btn_frame, text = PLAY, width = BTN_W, command = self.launch_video)
		self.btn_launch_video.grid(row = 1, column = 0, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		# Кнопка "Пауза"
		self.btn_pause_video = Button(btn_frame, text = PAUSE, width = BTN_W, command = self.pause_video)
		self.btn_pause_video.grid(row = 1, column = 1, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		# Кнопка "Поновити"
		self.btn_relaunch_video = Button(btn_frame, text = RELAUNCH, width = BTN_W, command = self.relaunch_video)
		self.btn_relaunch_video.grid(row = 1, column = 2, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		# Кнопка "Скріншот"
		self.btn_take_a_snapshot = Button(btn_frame, text = SNAPSHOT, width = BTN_W, command = self.take_a_snapshot)
		self.btn_take_a_snapshot.grid(row = 1, column = 3, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		self.delay = 15   # ms
		self.window.mainloop()


	# Відкрити відеозапис	
	def open_video(self):
		self.pause = False

		#self.filename = filedialog.askopenfilename(title = SELECT_VIDEO,
		#	initialdir = VIDEOS_FOLDER,
		#	filetypes = VIDEOTYPES)
		#self.filename = self.helper.get_videofile() 
		
		self.selected_video = self.helper.get_videofile()

		if self.selected_video:
			self.helper.remove_old_snapshots(SNAPSHOTS_FOLDER)

			# fix the canvas
			self.cap = cv2.VideoCapture(self.selected_video)
			self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
			self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
			
			# Полотно для відео
			if 0 < self.width <= 860 and 0 < self.height <= 480:
					messagebox.showinfo(message = LAUNCH) 
					self.canvas.config(width = self.width, height = self.height)
			else:
					messagebox.showerror(title = TITLE_ERROR, message = CANT_DISPLAY_VIDEO)						
		else:
			self.selected_video = None

	def update_photo_collection(self):
		out = subprocess.check_output(DISKS_CAPTIONS, shell = True) 
		PATHS_TO_NEW_IMGS = ""
		for drive in str(out).strip().split('\\r\\r\\n'):
			if '2' in drive:
				drive_letter = drive.split(':')[0]
				if drive_letter not in ('C', 'D'): # Флешку вставлено?
					PATHS_TO_NEW_IMGS = f"{drive_letter}:/photos"
					break
		try: 
			new_photos = os.listdir(PATHS_TO_NEW_IMGS)
			for n in new_photos:
				if n.endswith(('jpg', 'png', 'gif')):
					copyfile(f"{PATHS_TO_NEW_IMGS}/{n}", f"{PHOTOS_FOLDER}/{n}")
		except:
			messagebox.showerror(title = TITLE_ERROR, message = CANT_ADD_IMGS)

	# Зчитати кадр з відео		
	def get_frame(self):
		try:
			if self.cap.isOpened():
				ret, frame = self.cap.read()
				return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
		except:
			messagebox.showerror(title = TITLE_ERROR, message = CANT_LAUNCH)					

	def launch_video(self):
		try:
			if self.selected_video is None:
				messagebox.showerror(title = TITLE_ERROR, message = NOT_SELECTED)
				return				
			self.launch = True

			# Зчитування кадрів з відео
			ret, frame = self.get_frame()

			if ret:
				self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
				self.canvas.create_image(0, 0, image = self.photo, anchor = NW)

			if not self.pause:
				self.window.after(self.delay, self.launch_video)
		except:
			pass

	def pause_video(self):
		if self.pause == True:
			pass
		if self.selected_video is None:
			messagebox.showerror(title = TITLE_ERROR, message = NOT_SELECTED)

		self.pause = True

	def relaunch_video(self):
		self.pause = False
		self.launch_video()

	def take_a_snapshot(self):
		if self.selected_video is None or self.launch == False:
			messagebox.showerror(title = TITLE_ERROR, message = NOT_SELECTED)
			return

		ret, frame = self.get_frame()	
		if ret:
			#cv2.imwrite(os.path.join(SNAPSHOTS_FOLDER, "frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
			cv2.imwrite(os.path.join(SNAPSHOTS_FOLDER, "frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
			

	def recognize_faces(self):
		pass

	def __del__(self):
		try:
			if self.cap.isOpened():
				self.cap.release()
		except:
			pass			