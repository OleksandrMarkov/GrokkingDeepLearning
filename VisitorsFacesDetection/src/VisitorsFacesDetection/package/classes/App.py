from tkinter import *
#from tkinter import messagebox
from package.constants import *
from tkinter import filedialog
#from shutil import copyfile, ignore_patterns

from package.classes.Helper import *
from package.classes.Alerts import *

import PIL.Image, PIL.ImageTk
import cv2
import face_recognition  #pip install dlib & pip install face-recognition 

import os, shutil

import time

class App():
	def __init__(self, window):

		self.helper = Helper()
		self.error = Error()
		self.info = Info()

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

		# Керування кнопкою "Пауза"
		self.pause = False

		self.canvas = Canvas(top_frame)
		self.canvas.pack()

		# Кнопка "Відеозапис"
		self.btn_select_video = Button(btn_frame, text = SELECT_VIDEO, width = BTN_W, command = self.open_video)
		self.btn_select_video.grid(row = 0, column = 0, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		# Кнопка "Розпізнавання"
		self.btn_recognize_faces = Button(btn_frame, text = START_RECOGNITION, width = BTN_W, command = self.recognize_faces)
		self.btn_recognize_faces.grid(row = 0, column = 1, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		# Кнопка "Оновити колекцію зображень"
		self.btn_update_photo_collection = Button(btn_frame, text = NEW_IMAGES, width = BTN_W, command = self.update_photo_collection)
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


	def frames_are_of_acceptable_size(self, selected_video):
		self.cap = cv2.VideoCapture(selected_video) 
		canvas_width, canvas_height = self.get_frame_size(selected_video)

		if MAX_FRAME_WIDTH >= canvas_width > 0 and MAX_FRAME_HEIGHT >= canvas_height > 0:
			#print(canvas_width)
			#print(canvas_height)
			return True
		return False	
	
	def get_frame_size(self, selected_video):
		cap = cv2.VideoCapture(selected_video)
		canvas_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
		canvas_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
		return canvas_width, canvas_height

	def configure_the_canvas(self, canvas, selected_video):
		return canvas.config(width = self.get_frame_size(selected_video)[0],
			height = self.get_frame_size(selected_video)[1])

	# Відкрити відеозапис	
	def open_video(self):
		self.pause = False
		
		self.selected_video = self.helper.get_videofile()

		if self.selected_video:
			self.helper.remove_old_snapshots(SNAPSHOTS_FOLDER)

			# configure the canvas			
			if self.frames_are_of_acceptable_size(self.selected_video):
				self.info.show(message = LAUNCH)
				#messagebox.showinfo(message = LAUNCH)
				self.configure_the_canvas(self.canvas, self.selected_video)
			else:
				#messagebox.showerror(title = TITLE_ERROR, message = CANT_DISPLAY_VIDEO)
				self.error.show(message = CANT_DISPLAY_VIDEO)
		else:
			self.selected_video = None

	def update_photo_collection(self):
		path_to_new_collection = self.helper.get_path_to_new_collection()

		if path_to_new_collection is not None:
			try:
				self.helper.move_images(path_to_new_collection)
			except:
				self.error.show(message = CANT_ADD_IMAGES)

	# Зчитати кадр з відео		
	def get_frame(self):
		try:
			if self.cap.isOpened():
				ret, frame = self.cap.read()
				return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
		except:
			#messagebox.showerror(title = TITLE_ERROR, message = CANT_LAUNCH)
			self.error.show(message = CANT_LAUNCH)					

	def launch_video(self):
		try:
			if self.selected_video is None:
				self.error.show(message = NOT_SELECTED)
				#messagebox.showerror(title = TITLE_ERROR, message = NOT_SELECTED)
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
			self.error.show(message = NOT_SELECTED)
			#messagebox.showerror(title = TITLE_ERROR, message = NOT_SELECTED)

		self.pause = True

	def relaunch_video(self):
		self.pause = False
		self.launch_video()

	def take_a_snapshot(self):
		if self.selected_video is None or self.launch == False:
			self.error.show(message = NOT_SELECTED)
			#messagebox.showerror(title = TITLE_ERROR, message = NOT_SELECTED)
			return

		ret, frame = self.get_frame()	
		if ret:
			#cv2.imwrite(os.path.join(SNAPSHOTS_FOLDER, "frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
			cv2.imwrite(os.path.join(SNAPSHOTS_FOLDER, "frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
			

	def recognize_faces(self):
		if self.selected_video is None:
			self.error.show(message = NOT_SELECTED)
		else:
			pass
			# CROP IMAGES -> CV2GRAY -> ENCODINGS

			# FRAMES CYCLE : LOCATIONS/ENCODINGS -> COMPARING
			
			#self.helper.crop_images_from_the_collection()

	def __del__(self):
		try:
			if self.cap.isOpened():
				self.cap.release()
		except:
			pass			