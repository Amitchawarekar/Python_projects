from tkinter import *
from tkinter import ttk, Frame
from PIL import Image,ImageTk
from tkinter import messagebox as tsmg
import mysql.connector
import cv2
import warnings
import os
import csv
from tkinter import filedialog
warnings.filterwarnings('ignore')

mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #=============text variables ===================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time= StringVar()
        self.var_atten_date= StringVar()
        self.var_atten_attendance = StringVar()

        # First Image
        img = Image.open("images/student-management-system.jpg")
        img = img.resize((800, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # Second Image
        img1 = Image.open("images/images6.jpg")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        # bg Image
        img3 = Image.open("images/blue-dark-gradient-texture-wall-background_28629-888.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="Attendance Management System", font=('lucida', 35, "bold"),
                          bg='green', fg='white')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg='white')
        main_frame.place(x=20, y=50, width=1480, height=600)

        # left  label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text='Student Attendance Details',
                                font=('lucida', 12, 'bold'))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img4 = Image.open("images/student-management-system.jpg")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(Left_frame, image=self.photoimg4)
        bg_img.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame,relief =RIDGE,bd=2, bg='white')
        left_inside_frame.place(x=0, y=135, width=720, height=370)

        #=========labels and entry ===================

        # attnendance ID
        attendanceID_lbl = Label(left_inside_frame, text="StudentID:", bg='white', font=('lucida', 12, 'bold'))
        attendanceID_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame,  width=20,textvariable=self.var_atten_id,font=('lucida', 12, 'bold'))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # roll
        rollLabel = Label(left_inside_frame, text="Roll:", bg='white', font=('lucida', 12, 'bold'))
        rollLabel.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        rollEntry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_roll, font=('lucida', 12, 'bold'))
        rollEntry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # student name
        studentName_lbl = Label(left_inside_frame, text="Student Name:", bg='white', font=('lucida', 12, 'bold'))
        studentName_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(left_inside_frame,  width=20,textvariable=self.var_atten_name,font=('lucida', 12, 'bold'))
        studentName_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)



        # Department
        deplabel = Label(left_inside_frame, text="Department:", bg='white', font=('lucida', 12, 'bold'))
        deplabel.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        depEntry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep,font=('lucida', 12, 'bold'))
        depEntry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # time
        timeLabel = Label(left_inside_frame, text="Time:", bg='white', font=('lucida', 12, 'bold'))
        timeLabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        timeEntry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_time,font=('lucida', 12, 'bold'))
        timeEntry.grid(row=2, column=1, padx=10, pady=5, sticky=W)


        # date
        dateLabel = Label(left_inside_frame, text="Date:", bg='white', font=('lucida', 12, 'bold'))
        dateLabel.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dateEntry = ttk.Entry(left_inside_frame,  width=20,textvariable=self.var_atten_date,font=('lucida', 12, 'bold'))
        dateEntry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Course
        attendance_label = Label(left_inside_frame, text="Attendance Status", bg='white', font=('lucida', 12, 'bold'))
        attendance_label.grid(row=3, column=0, padx=10, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, font=('lucida', 12, 'bold'),textvariable=self.var_atten_attendance, width=17,
                                    state='readonly')
        self.atten_status ["values"] = ("Status","Present","Absent")
        self.atten_status.grid(row=3, column=1, padx=2, pady=10, sticky=W)
        self.atten_status.current(0)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame.place(x=0, y=300, width=715, height=35)

        import_btn = Button(btn_frame, text="Import csv",command =self.import_csv,width=17, font=('lucida', 13, 'bold'),
                          bg='blue', fg='white')
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export csv",command=self.export_csv, width=17, font=('lucida', 13, 'bold'),
                            bg='blue', fg='white')
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=17, font=('lucida', 13, 'bold'),
                            bg='blue', fg='white')
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset, width=17, font=('lucida', 13, 'bold'),
                           bg='blue', fg='white')
        reset_btn.grid(row=0, column=3)




        # right  label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text='Attendance',
                                 font=('lucida', 12, 'bold'))
        Right_frame.place(x=750, y=10, width=720, height=580)

        # =======================Table Frame ==============================
        Table_frame = Frame(Right_frame, bd=2, bg='white', relief=RIDGE)
        Table_frame.place(x=5, y=5, width=700, height=455)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', background='white', font=('Arial', 12), foreground='black', rowheight=28,
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', 'green')])
        self.attendance_table = ttk.Treeview(Table_frame, columns=("id","roll","name","department","time","date","attendance"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("id", text="Attendance ID")
        self.attendance_table.heading("roll", text="Rollno")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("department", text="Department")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("attendance", text="Attendance")

        self.attendance_table['show'] = "headings"
        self.attendance_table.column("id", width=150)
        self.attendance_table.column("roll", width=150)
        self.attendance_table.column("name", width=150)
        self.attendance_table.column("department", width=150)
        self.attendance_table.column("time", width=150)
        self.attendance_table.column("date", width=150)
        self.attendance_table.column("attendance", width=150)

        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)
        self.attendance_table.pack(fill=BOTH, expand=1)

    #============== fetch Data ======================================
    def fetch_data(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)

    #=====import csv ==========================
    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetype =( ("CSV File",".csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csv_read = csv.reader(myfile,delimiter=",")
            for i in csv_read:
                mydata.append(i)
            self.fetch_data(mydata)

    #==========export csv =========================
    def export_csv(self):
        try:
            if len(mydata) <1:
                tsmg.showerror("Error","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open csv",
                                             filetype=(("CSV File", ".csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                tsmg.showinfo("Data Export","Your Data Exported to" + os.path.basename(fln) + "successfully",parent=self.root)
        except Exception as es:
            tsmg.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    def update_data(self):
        try:
            if len(mydata) < 1:
                tsmg.showerror("Error", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open csv",
                                               filetype=(("CSV File", ".csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                tsmg.showinfo("Data Export", "Your Data Exported to" + os.path.basename(fln) + "successfully",
                              parent=self.root)
        except Exception as es:
            tsmg.showerror("Error", f"Due to :{str(es)}", parent=self.root)
    def get_cursor(self, event=''):
        cursor_focus = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_focus)
        data = content['values']
        self.var_atten_id.set(data[0]),
        self.var_atten_roll.set(data[1]),
        self.var_atten_name.set(data[2]),
        self.var_atten_dep.set(data[3]),
        self.var_atten_time.set(data[4]),
        self.var_atten_date.set(data[5]),
        self.var_atten_attendance.set(data[6]),

    def reset(self):
        self.var_atten_id.set(""),
        self.var_atten_roll.set(""),
        self.var_atten_name.set(""),
        self.var_atten_dep.set(""),
        self.var_atten_time.set(""),
        self.var_atten_date.set(""),
        self.var_atten_attendance.set(""),


if __name__ == "__main__":
    root =Tk()
    obj = Attendance(root)
    root.mainloop()
