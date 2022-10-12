
from tkinter import *
#from tkinter.ttk import *

import tkinter as tk
#from tkinter import ttk


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

    	btns_frame = Frame()
    	btns_frame.pack()

    	btn_select_video = Button(self, text="Select video", width = 10, height = 10, font = ('Arial', 20, 'bold'), bg='#567', fg='White', command = select_video)
    	btn_select_video.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()