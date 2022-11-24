from tkinter import messagebox
from package.constants import *

import telebot
import time, os

class Error:
	def show(self, message):
		messagebox.showerror(title = TITLE_ERROR, message = message)

class Info:
	def show(self, message):
		messagebox.showinfo(message = message)

class Report():
	def __init__(self, captured_visitors):
		self.time = time.strftime("%d.%m.%Y %H:%M:%S")
		self.visitors = captured_visitors

	def get_amount_of_snapshots(self):
		return len([entry for entry in os.listdir(SNAPSHOTS)\
		 if os.path.isfile(os.path.join(SNAPSHOTS, entry))])

	def no_visitors(self):
		if len(self.visitors) == 0:
			return True
		return False

	def send(self):
		bot = telebot.TeleBot(TOKEN)
		bot.send_message(TG_USER, self.time)

		if self.get_amount_of_snapshots() == 0:
			self.about_snapshots = "Окремих скріншотів для відео не створено." 
			bot.send_message(TG_USER, self.about_snapshots)
		else:
			self.about_snapshots = f"Додаткових скріншотів: {self.get_amount_of_snapshots()}"
			
			for (root, dirs, snapshots) in os.walk(SNAPSHOTS):
				for snapshot_name in snapshots:
					path = os.path.join(root, snapshot_name).replace("\\", "/")
					photo = open(path, 'rb')
					bot.send_photo(TG_USER, photo)
		
		if self.no_visitors():
			self.about_recognition = "Визначених відвідувачів з колекції зображень на відео не зафіксовано..."
			bot.send_message(TG_USER, self.about_recognition)
		else:
			self.about_recognition = f"Фото ідентифікованих відвідувачів на відео: {len(self.visitors)}."
			bot.send_message(TG_USER, self.about_recognition)
			for visitor in self.visitors:
				photo = open(visitor.path, 'rb')
				bot.send_photo(TG_USER, photo)