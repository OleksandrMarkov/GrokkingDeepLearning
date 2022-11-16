from tkinter import messagebox
from package.constants import *

class Error:
	def show(self, message):
		messagebox.showerror(title = TITLE_ERROR, message = message)

class Info:
	def show(self, message):
		messagebox.showinfo(message = message)	