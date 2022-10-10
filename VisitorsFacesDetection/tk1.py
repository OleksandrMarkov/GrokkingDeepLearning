#import tkinter as tk
from tkinter import *
from tkinter.ttk import *

# window features
window = Tk()
window.title("Face recognition in videos")
window['background']='#f2dbff'
window.iconbitmap('ico/icon.ico')
window_width, window_height = 800, 500
screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
center_x, center_y = int(screen_width/2 - window_width/2), int(screen_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.resizable(False, False)
window.attributes('-topmost', 1)

frame = Frame()
frame.pack()

#greeting = tk.Label(text="Hello, Tkinter")
#greeting.pack()
#window.iconphoto(False, tk.PhotoImage(file='/ico/icon.ico'))

window.mainloop()