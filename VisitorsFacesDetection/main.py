from tkinter import *
from tkinter import messagebox

from package.constants import *

from tkinter import filedialog

from shutil import copyfile, ignore_patterns

import PIL.Image, PIL.ImageTk
import cv2
import os
import subprocess # detect USB flash drive
import time

class App:
    def __init__(self, window):

        self.window = window
        self.window.title(WINDOW_TITLE)
        #self.window['background'] = WINDOW_BACKGROUND
        self.window.iconbitmap(ICON)
        self.window.resizable(False, False)

        #window_width, window_height = 700, 500
        #screen_width, screen_height = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        #center_x, center_y = int(screen_width/2 - window_width/2), int(screen_height/2 - window_height/2)
        #self.window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


        self.launch = False 
        self.selected_video = None 

        # Block for selected video
        top_frame = Frame(self.window)
        #top_frame.pack_propagate(False)
        top_frame.pack(side = TOP, pady = 10)

        # Block for buttons
        btn_frame = Frame(self.window, bg = BTN_FRAME_COLOR)
        btn_frame.pack(side = BOTTOM, pady = 5)

        self.pause = False   # Parameter that controls 'Pause' button

        self.canvas = Canvas(top_frame)
        self.canvas.pack()

        # 'Select' Button
        self.btn_select = Button(btn_frame, text = SELECT_VIDEO, width = BTN_W, command = self.open_video)
        self.btn_select.grid(row = 0, column = 0, ipadx = 6, ipady = 6, padx = 5, pady = 5)

        # 'Recognize' Button
        self.btn_recognize = Button(btn_frame, text = START_RECOGNITION, width = BTN_W, command = self.recognize_face)
        self.btn_recognize.grid(row = 0, column = 1, ipadx = 6, ipady = 6, padx = 5, pady = 5)

        # 'Add photos' button
        self.btn_add_photos = Button(btn_frame, text = NEW_IMGS, width = BTN_W, command = self.add_photos)
        self.btn_add_photos.grid(row = 0, column = 2, ipadx = 6, ipady = 6, padx = 5, pady = 5)

        # 'FAQ' Button
        self.btn_faq = Button(btn_frame, text = FAQ, width = BTN_W)
        self.btn_faq.grid(row = 0, column = 3, ipadx = 6, ipady = 6, padx = 5, pady = 5)

        # 'Launch' Button
        self.btn_launch = Button(btn_frame, text = PLAY, width = BTN_W, command = self.launch_video)
        self.btn_launch.grid(row = 1, column = 0, ipadx = 6, ipady = 6, padx = 5, pady = 5)

        # 'Pause' Button
        self.btn_pause = Button(btn_frame, text = PAUSE, width = BTN_W, command = self.pause_video)
        self.btn_pause.grid(row = 1, column = 1, ipadx = 6, ipady = 6, padx = 5, pady = 5)

        # 'Relaunch' Button
        self.btn_relaunch = Button(btn_frame, text = RELAUNCH, width = BTN_W, command = self.relaunch_video)
        self.btn_relaunch.grid(row = 1, column = 2, ipadx = 6, ipady = 6, padx = 5, pady = 5)

        # 'Screenshot' Button
        self.btn_screenshot = Button(btn_frame, text = SCREENSHOT, width = BTN_W, command = self.screenshot_video)
        self.btn_screenshot.grid(row = 1, column = 3, ipadx = 6, ipady = 6, padx = 5, pady = 5)

        self.delay = 15   # ms

        self.window.mainloop()

    def open_video(self):

        self.pause = False

        self.filename = filedialog.askopenfilename(title = SELECT_VIDEO,
            initialdir = VIDEOS_FOLDER,
            filetypes = VIDEOTYPES)
        
        self.selected_video = self.filename
        
        if self.selected_video:
            messagebox.showinfo(message = LAUNCH)
        else:
            self.selected_video = None

        # Open the video file
        self.cap = cv2.VideoCapture(self.selected_video)

        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # Canvas for the video
        if self.width > 0 and self.height > 0:
            self.canvas.config(width = self.width, height = self.height)

    def add_photos(self):
        out = subprocess.check_output(DISKS_CAPTIONS, shell = True) 
        WAY_TO_NEW_IMGS = ""
        for drive in str(out).strip().split('\\r\\r\\n'):
            if '2' in drive:
                drive_letter = drive.split(':')[0]
                #drive_type = drive.split(':')[1].strip()
                if drive_letter not in ('C', 'D'): # there is a flash drive
                    WAY_TO_NEW_IMGS = f"{drive_letter}:/photos"
                    break
        try: 
            new_photos = os.listdir(WAY_TO_NEW_IMGS)
            for n in new_photos:
                if n.endswith(('jpg', 'png', 'gif')):
                    copyfile(f"{WAY_TO_NEW_IMGS}/{n}", f"{PHOTOS_FOLDER}/{n}")
        except:
            messagebox.showerror(title = TITLE_ERROR, message = CANT_ADD_IMGS)

    def get_frame(self):   # get only one frame
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
            # Get a frame from the video source, and go to the next frame automatically
            ret, frame = self.get_frame()

            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image = self.photo, anchor = NW)

            if not self.pause:
                self.window.after(self.delay, self.launch_video)
        except:
            pass

    def pause_video(self):
        #if self.pause == True:
        #    messagebox.showerror(title=TITLE_ERROR, message = NOT_SELECTED)
        #if self.selected_video is None:
        #    messagebox.showerror(title=TITLE_ERROR, message=NOT_SELECTED)
        #    return
        if self.pause == True or self.selected_video is None: 
            messagebox.showerror(title = TITLE_ERROR, message = NOT_SELECTED)
        self.pause = True

    def relaunch_video(self):
        #if self.pause == False:
        #    messagebox.showerror(title='Виникла помилка!', message='Відеофайл не відтворюється!')
        self.pause = False
        self.launch_video()

    def screenshot_video(self):
        if self.selected_video is None or self.launch == False:
            messagebox.showerror(title = TITLE_ERROR, message = NOT_SELECTED)
            return

        ret, frame = self.get_frame()    
        if ret:
            cv2.imwrite(os.path.join(SCREENSHOTS_FOLDER, "frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def recognize_face(self):
        if self.selected_video is None:
            messagebox.showerror(title = TITLE_ERROR, message = NOT_SELECTED)
            return
        else:
            try: 
                # Process all images from photos folder except processed photos
                for (root, dirs, imgs) in os.walk(PHOTOS_FOLDER):                        
                    for img_name in imgs:
                        if (".jpg" in img_name or ".png" in img_name or ".gif" in img_name) and (PROCESSED_PHOTOS_FOLDER not in os.path.join(root, img_name)):
                            # Firstly leave only face on photo

                            #print(os.path.join(root, img_name).replace('\\', '/')) # dataset/photos/gilardino7we8sp_971483767_1_add.png
                            #print(img_name) # gilardino7we8sp_971483767_1_add.png

                            img = cv2.imread(rf"{PHOTOS_FOLDER}/{img_name}")

                            model = cv2.CascadeClassifier(FACE_RECOG_MODEL) 
                            faces = model.detectMultiScale(img, scaleFactor = 1.1, minNeighbors = 2)
                            if len(faces) != 0:
                                for index, (x,y,w,h) in enumerate(faces):
                                    img = img[x:y+h]
                                    if ".jpg" in img_name:
                                        cv2.imwrite(f"{PROCESSED_PHOTOS_FOLDER}/{img_name}", img) # "tmp.jpg" 
                                    elif ".png" in img_name:
                                        cv2.imwrite(f"{PROCESSED_PHOTOS_FOLDER}/{img_name}", img) # "tmp.png" 
                                    else:
                                        cv2.imwrite(f"{PROCESSED_PHOTOS_FOLDER}/{img_name}", img) # "tmp.gif" 
                messagebox.showinfo(message = "All photos are processed!")            
            except:
                pass    

    # Release the video source when the object is destroyed
    def __del__(self):
        try:
            if self.cap.isOpened():
                self.cap.release()
        except:
            pass
                
# Create a window and pass it to App Class
App(Tk())