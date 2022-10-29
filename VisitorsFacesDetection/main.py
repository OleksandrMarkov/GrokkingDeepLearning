from tkinter import *
from tkinter import messagebox

from package.constants import *

from tkinter import filedialog
import PIL.Image, PIL.ImageTk
import cv2
import os
import subprocess # detect USB
import time

class videoGUI:

    def __init__(self, window):

        self.window = window
        self.window.title(WINDOW_TITLE)
        self.window['background'] = WINDOW_BACKGROUND
        self.window.iconbitmap(ICON)
        self.window.resizable(False, False)

        self.play = False
        self.selected_video = None 


        top_frame = Frame(self.window) # width = 0, height = 0
        #top_frame.pack_propagate(False)
        #top_frame['background'] = '#7f7aff'
        top_frame.pack(side=TOP, pady = 10)

        #label1 = Label(top_frame, text="Виберіть відеофайл для початку роботи")
        #label1.pack()

        btn_frame = Frame(self.window, bg= BTN_FRAME_COLOR)
        btn_frame.pack(side=BOTTOM, pady=5)

        self.pause = False   # Parameter that controls pause button

        self.canvas = Canvas(top_frame)
        self.canvas.pack()

        # Select Button
        self.btn_select=Button(btn_frame, text=SELECT_VIDEO, width = BTN_W, command=self.open_file)
        self.btn_select.grid(row=0, column=0, ipadx=6, ipady=6, padx=5, pady=5)

        self.btn_recognize = Button(btn_frame, text=START_RECOGNITION, width = BTN_W, command = self.recognize_face)
        self.btn_recognize.grid(row=0, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        self.btn_add_photo = Button(btn_frame, text=NEW_PHOTO, width = BTN_W, command = self.add_photo)
        self.btn_add_photo.grid(row=0, column=2, ipadx=6, ipady=6, padx=5, pady=5)

        self.btn_faq = Button(btn_frame, text=FAQ, width = BTN_W)
        self.btn_faq.grid(row=0, column=3, ipadx=6, ipady=6, padx=5, pady=5)

        # Play Button
        self.btn_play=Button(btn_frame, text=PLAY, width = BTN_W, command=self.play_video)
        self.btn_play.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)

        # Pause Button
        self.btn_pause=Button(btn_frame, text=PAUSE, width = BTN_W, command=self.pause_video)
        self.btn_pause.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Resume Button
        self.btn_resume=Button(btn_frame, text=CONTINUE, width = BTN_W, command=self.resume_video)
        self.btn_resume.grid(row=1, column=2, ipadx=6, ipady=6, padx=5, pady=5)

        # Screenshot Button
        self.btn_screenshot = Button(btn_frame, text=SCREENSHOT, width = BTN_W, command=self.screenshot_video)
        self.btn_screenshot.grid(row=1, column=3, ipadx=6, ipady=6, padx=5, pady=5)

        self.delay = 15   # ms

        self.window.mainloop()


    def open_file(self):

        self.pause = False

        self.filename = filedialog.askopenfilename(title = SELECT_FILE,
            initialdir = VIDEOS_FOLDER,
            filetypes = VIDEOTYPES)
        
        self.selected_video = self.filename
        
        if self.selected_video:
            messagebox.showinfo(message = START_WORK)
        else:
            self.selected_video = None
        #print(self.filename)

        # Open the video file
        self.cap = cv2.VideoCapture(self.selected_video)

        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        if self.width > 0 and self.height > 0:
            self.canvas.config(width = self.width, height = self.height)
        #print(self.width)
        #print(self.height)

    def add_photo(self):
        out = subprocess.check_output('wmic logicaldisk get  DriveType, caption', shell=True)
        for drive in str(out).strip().split('\\r\\r\\n'):
            if '2' in drive:
                # check with two flash usb drives
                drive_letter = drive.split(':')[0]
                drive_type = drive.split(':')[1].strip()
                print(drive_letter, drive_type)
            
        
    def get_frame(self):   # get only one frame
        try:

            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        except:
            messagebox.showerror(title = TITLE_ERROR, message = CANT_START)                    



    def play_video(self):
        try:
            if self.selected_video is None:
                messagebox.showerror(title = TITLE_ERROR, message = NOT_SELECTED)
                return                
            self.play = True
            # Get a frame from the video source, and go to the next frame automatically
            ret, frame = self.get_frame()

            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image = self.photo, anchor = NW)

            if not self.pause:
                self.window.after(self.delay, self.play_video)
        except:
            pass

    def pause_video(self):
        #if self.pause == True:
        #    messagebox.showerror(title=TITLE_ERROR, message = NOT_SELECTED)
        #if self.selected_video is None:
        #    messagebox.showerror(title=TITLE_ERROR, message=NOT_SELECTED)
        #    return
        if self.pause == True or self.selected_video is None: 
            messagebox.showerror(title=TITLE_ERROR, message=NOT_SELECTED)
        self.pause = True

    #Resume
    def resume_video(self):
        #if self.pause == False:
        #    messagebox.showerror(title='Виникла помилка!', message='Відеофайл не відтворюється!')
        self.pause=False
        self.play_video()

    def screenshot_video(self):
        if self.selected_video is None or self.play == False:
            messagebox.showerror(title=TITLE_ERROR, message=NOT_SELECTED)
            return

        ret, frame = self.get_frame()    
        if ret:
            cv2.imwrite(os.path.join(SCREENSHOTS_FOLDER, "frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))



    def recognize_face(self):
        if self.selected_video is None:
            messagebox.showerror(title=TITLE_ERROR, message=NOT_SELECTED)
            return        

    # Release the video source when the object is destroyed
    def __del__(self):
        try:
            if self.cap.isOpened():
                self.cap.release()
        except:
            pass
                
# Create a window and pass it to videoGUI Class
videoGUI(Tk())