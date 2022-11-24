from tkinter import messagebox
from package.constants import *

import time

class Error:
	def show(self, message):
		messagebox.showerror(title = TITLE_ERROR, message = message)

class Info:
	def show(self, message):
		messagebox.showinfo(message = message)

class Report():
	def __init__(self, captured_visitors, snapshots_amount):
		self.time = time.strftime("%d-%m-%Y-%H-%M-%S")			