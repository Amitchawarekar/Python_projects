from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tsmg
import numpy as np
from PIL import Image,ImageTk
from student import Student
import cv2
import os
import mysql.connector

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATASET", font=('lucida', 35, "bold"),
                          bg='orange', fg='white')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open("images/blue-dark-gradient-texture-wall-background_28629-888.jpg")
        img_top = img_top.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=5, y=50, width=1530, height=325)

        #==Button===========
        train_btn = Button(self.root, text="TRAIN DATA",command=self.train_classifier,width=17, font=('lucida', 20, 'bold'),
                          bg='blue', fg='white')
        train_btn.place(x=0, y=377, width=1530, height=60)

        img_bottom = Image.open("images/employee_bg_image.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl1 = Label(self.root, image=self.photoimg_bottom)
        f_lbl1.place(x=5, y=440, width=1530, height=325)


    def train_classifier(self):
        data_dir = ('data')
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces =[]
        ids = []

        for image in path:
            img = Image.open(image).convert('L') #Gray Scale Conversion
            imageNP = np.array((img))
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        #================== Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        tsmg.showinfo('Result',"Training Dataset Completed!!",parent=self.root)












if __name__ == "__main__":
    root =Tk()
    obj = Train(root)
    root.mainloop()