
from tkinter import *
import tkinter as tk

from tkinter import ttk


def select_video():
	btn_select_video['fg'] = 'Green'


class App(tk.Tk):
	def __init__(self):
		super().__init__()

		# window features
		self.title("Face recognition in videos")
		self['background']='#f2dbff'
		self.iconbitmap('ico/icon.ico')
		self_width, self_height = 800, 500
		screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
		center_x, center_y = int(screen_width/2 - self_width/2), int(screen_height/2 - self_height/2)
		self.geometry(f'{self_width}x{self_height}+{center_x}+{center_y}')
		self.resizable(width = False, height = False)
		self.attributes('-topmost', 1)

		self.option_add("*tearOff", FALSE) # not using a dotted line in menu

		self.rowconfigure(0, weight=1) # menu
		self.rowconfigure(1, weight=8) # photo_slider
		self.rowconfigure(0, weight=1) # additional row

		app_menu = Menu()
		
		data_menu = Menu()

		view_menu = Menu()
		rotate_menu = Menu()
		
		help_menu = Menu()
		language_menu = Menu()

		data_menu.add_command(label="New Video")
		data_menu.add_command(label="New Photo") # copy from USB flash drive
		data_menu.add_separator()
		data_menu.add_command(label="Exit")
		
		rotate_menu.add_command(label="Rotate Right 90°")
		rotate_menu.add_command(label="Rotate Left 90°")
		rotate_menu.add_command(label="Flip Vertical")
		rotate_menu.add_command(label="Flip Horizontal")

		view_menu.add_command(label="Full screen F11")
		view_menu.add_cascade(label="Rotate", menu=rotate_menu)
 		
		language_menu.add_command(label="Українська")
		language_menu.add_command(label="English")

		help_menu.add_cascade(label="Language", menu=language_menu) 
		help_menu.add_command(label="...")
		help_menu.add_command(label="FAQ")

		app_menu.add_cascade(label="Data", menu=data_menu)
		app_menu.add_cascade(label="View", menu=view_menu)
		app_menu.add_cascade(label="Help", menu=help_menu)
		
		self.config(menu=app_menu)
		
		#main_frame = ttk.Frame(self)
		#menu_frame = Frame(main_frame, height=0.1*self_height, borderwidth=2, relief=GROOVE, background="pink")
		#menu_frame.pack()		
		#menu_frame2 = Frame(main_frame, width=10, height=0.1*self_height, borderwidth=2, relief=GROOVE, background="yellow")
		#menu_frame2.pack(pady=8)
		#main_frame.pack(pady=8)

		#btns_frame = Frame(self, background="yellow")
		#btns_frame.grid(row=1, column=0, sticky="nsew")
		

		#btn_select_video = Button(self, text="Select video", width = 10, height = 10, font = ('Arial', 20, 'bold'), bg='#567', fg='White', command = select_video)
		#btn_select_video.pack()

if __name__ == "__main__":
	app = App()
	app.mainloop()