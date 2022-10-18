import tkinter as tk
from tkinter import *
from tkinter import ttk
import cv2
import PIL.Image, PIL.ImageTk
import time

from tkinter import filedialog as fd
from tkinter.messagebox import showerror, showwarning, showinfo


class App:
	def select_video(self):
		#showinfo("GUI Python", "select_video")
		filetypes = (
			('mp4 video files', '*.mp4'),
			('avi video files', '*.avi')
			)

		filename = fd.askopenfilename(
		title='Open a video file',
		initialdir='C:/Users/ALEX/Documents/grokkingDeepLearning/VisitorsFacesDetection/dataset/videos',
		filetypes=filetypes)

		self.video_source = filename.split("/videos/")[1].strip()
		print(self.video_source)

		win2 = tk.Tk()
		# open video source (by default this will try to open the computer webcam)
		vid = MyVideoCapture("file_example.mp4") # self.video_source
		# Create a canvas that can fit the above video source size
		win2.canvas = tk.Canvas(width = vid.width, height = vid.height)
		#self.video_frame
		win2.canvas.pack()
		win2.delay = 15
		win2.update()
		win2.mainloop()
		


		# absolute path to the file
		#showinfo(
		#title='Selected video',
		#message = filename.split("/videos/")[1] 
    	#)


	def __init__(self, window, video_source="file_example.mp4"):
		self.window = window
		self.window.title("Face recognition in videos")
		self.window.background = "f2dbff"

		#window_width, window_height = 500, 500
		#screen_width, screen_height = self.window.winfo_screenwidth(), self.window.winfo_screenheight()		
		#center_x, center_y = int(screen_width/2 - window_width/2), int(screen_height/2 - window_height/2)
		#self.window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

		self.window.option_add("*tearOff", False) # not using a dotted line in menu


		menubar = Menu(self.window)
		
		data_menu = Menu(menubar, relief=FLAT, font=("Verdana", 12), bg = 'green', activebackground='red')
		data_menu.add_command(label="Нове відео", command = self.select_video)
		data_menu.add_command(label="Нове фото") # copy from USB flash drive
		data_menu.add_separator()
		data_menu.add_command(label="Вихід", command = self.window.quit)
		menubar.add_cascade(label="Дані", menu=data_menu)

		view_menu = Menu(menubar, relief=FLAT, font=("Verdana", 12), bg = 'orange', activebackground='sky blue')
		rotate_menu = Menu()

		help_menu = Menu()
		language_menu = Menu()

		rotate_menu.add_command(label="Rotate Right 90°")
		rotate_menu.add_command(label="Rotate Left 90°")
		rotate_menu.add_command(label="Flip Vertical")
		rotate_menu.add_command(label="Flip Horizontal")

		view_menu.add_command(label="Повний екран F11")
		view_menu.add_cascade(label="Rotate", menu=rotate_menu)
		 
		language_menu.add_command(label="Українська")
		language_menu.add_command(label="English")

		help_menu.add_cascade(label="Мова?", menu=language_menu) 
		help_menu.add_command(label="...")
		help_menu.add_command(label="FAQ")
	
		menubar.add_cascade(label="Вид", menu=view_menu)
		menubar.add_cascade(label="Допомога", menu=help_menu)

		self.window.config(menu=menubar)


		paddings = {'ipadx': 10, 'ipady': 10, 'padx': 10, 'pady': 10}
		
		# LABELS

		# Label that describes photos database
		self.photos_info = tk.Label(
			window,
			bg="green",
			fg="white",
			text = "В сховищі X зображень Y осіб.",
			font= ("Helvetica", 14)
			)
		self.photos_info.pack(**paddings, fill=tk.X)
		
		self.getting_started = tk.Label(
			window,
			bg="blue",
			fg="white",
			text = "Завантажте відеофайл (пункт меню \"Дані\")",
			font= ("Helvetica", 14)
			)
		self.getting_started.pack(**paddings, fill=tk.X)

		self.video_frame = tk.Frame(window)
		self.video_frame.pack(expand = True, fill = tk.BOTH, side = tk.LEFT)

		# BUTTONS

		# Button that lets the user start/stop video
		self.btn_start=tk.Button(window, text="Start", state=["disabled"], command=self.snapshot)
		self.btn_start.pack(**paddings, expand = True, fill = tk.BOTH, side = tk.LEFT)

		# Button that lets the user take a snapshot
		self.btn_snapshot=tk.Button(window, text="Snapshot", state=["disabled"], command=self.snapshot)
		#self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)
		self.btn_snapshot.pack(**paddings, expand = True, fill = tk.BOTH, side = tk.LEFT)

		# Button that lets the user share video
		self.btn_share=tk.Button(window, text="Share", state=["disabled"], command=self.snapshot)
		self.btn_share.pack(**paddings, expand = True, fill = tk.BOTH, side = tk.LEFT) 

		# After it is called once, the update method will be automatically called every delay milliseconds
		#self.delay = 15
		#self.update()
 
		self.window.mainloop()
	
		

	def snapshot(self):
		# Get a frame from the video source
		ret, frame = self.vid.get_frame()
 
		if ret:
			cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
 
	def update(self):
		# Get a frame from the video source
		ret, frame = self.vid.get_frame()
		if ret:
			self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
			self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
		self.window.after(self.delay, self.update)
 
 
class MyVideoCapture:
	def __init__(self, video_source): # video_source="file_example.mp4"
		# Open the video source
		self.vid = cv2.VideoCapture(video_source)
		if not self.vid.isOpened():
			raise ValueError("Unable to open video source", video_source)
		#try:
		#	self.vid = cv2.VideoCapture(video_source)
		#except Exception as e:
		#	print(e)
 
		# Get video source width and height
		self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
	def get_frame(self):
		if self.vid.isOpened():
			ret, frame = self.vid.read()
			if ret:
			# Return a boolean success flag and the current frame converted to BGR
				return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
			else:
				return (ret, None)
		else:
			return (ret, None)
 
	# Release the video source when the object is destroyed
	def __del__(self):
		if self.vid.isOpened():
			self.vid.release()
 
# Create a window and pass it to the Application object
App(tk.Tk())