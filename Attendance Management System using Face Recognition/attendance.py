import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from datetime import datetime
from time import strftime
from attendance import Attendance
import cv2
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.state('zoomed')
        self.root.title("Face Recognition System")


        #First Image
        img = Image.open("images/attendance-heading3.jpg")
        img = img.resize((500,150),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=150)

        #Second Image
        img1= Image.open("images/attendance-heading4.jpg")
        img1= img1.resize((550, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=550, height=150)

        #Third Image
        img2 = Image.open("images/attendance-heading5.jpg")
        img2= img2.resize((490, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1050, y=0, width=490, height=150)

        # bg Image
        img3 = Image.open("images/blue-dark-gradient-texture-wall-background_28629-888.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1530, height=710)

        title_lbl  = Label(bg_img,text = " FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font= ('Bell MT',35,"bold"),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #================time =========================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(100, time)

        lbl = Label(title_lbl,font = ('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #Student Button
        img4 = Image.open("images/student_photo.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1= Button(bg_img,image = self.photoimg4,command=self.student_details,cursor='hand2')
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text='Student Details',command=self.student_details, cursor='hand2',font= ('goudy',15,"bold"),bg='dark blue',fg='white')
        b1_1.place(x=200, y=300, width=220, height=40)

        #Train Face button
        img8 = Image.open("images/training-image.png")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor='hand2',command=self.train_data)
        b5.place(x=500, y=100, width=220, height=220)

        b5_5 = Button(bg_img, text='Train Data', cursor='hand2',command=self.train_data, font=('goudy', 15, "bold"), bg='dark blue',
                      fg='white')
        b5_5.place(x=500, y=300, width=220, height=40)


        #Detect Face
        img5 = Image.open("images/Learn-Facial-Recognition-scaled.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor='hand2',command=self.face_data)
        b2.place(x=800, y=100, width=220, height=220)

        b2_2 = Button(bg_img, text='Face Detector',command=self.face_data ,cursor='hand2', font=('goudy', 15, "bold"), bg='dark blue',
                      fg='white')
        b2_2.place(x=800, y=300, width=220, height=40)

        # Attendance Report
        img6 = Image.open("images/attendance.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6,command=self.attendance_data, cursor='hand2')
        b3.place(x=1100, y=100, width=220, height=220)

        b3_3 = Button(bg_img, text='Attendance',command=self.attendance_data, cursor='hand2', font=('goudy', 15, "bold"), bg='dark blue',
                      fg='white')
        b3_3.place(x=1100, y=300, width=220, height=40)


        # Photos button
        img9 = Image.open("images/photos_gallery.png")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b9 = Button(bg_img, image=self.photoimg9, cursor='hand2',command=self.open_image)
        b9.place(x=500, y=400, width=220, height=220)

        b9_9 = Button(bg_img, text='Photos', cursor='hand2',command=self.open_image,font=('goudy', 15, "bold"), bg='dark blue',
                      fg='white')
        b9_9.place(x=500, y=600, width=220, height=40)

        # exit button
        img11 = Image.open("images/exit.png")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b11 = Button(bg_img, image=self.photoimg11, command=self.exit, cursor='hand2')
        b11.place(x=800, y=400, width=220, height=220)

        b11_11 = Button(bg_img, text='Exit', cursor='hand2', command=self.exit, font=('goudy', 15, "bold"),
                        bg='dark blue',
                        fg='white')
        b11_11.place(x=800, y=600, width=220, height=40)



    #=======Functions for photos button================
    def open_image(self):
        os.startfile("data")
    #====================Functions Buttons ===============================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app =Attendance(self.new_window)

    def exit(self):
        self.iexit = tkinter.messagebox.askyesno("Face Recognitiom","Are you sure exit this project")
        if self.iexit >0:
            self.root.destroy()
        else:
            return



if __name__ == "__main__":
    root =Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
