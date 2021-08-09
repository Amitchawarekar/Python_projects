from tkinter import *
from tkinter import ttk, Frame
from PIL import Image,ImageTk
from tkinter import messagebox as tsmg
import mysql.connector
import cv2
import warnings
warnings.filterwarnings('ignore')

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #==========Variables ======================
        self.var_dep =StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_stdID = StringVar()
        self.var_stdName = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # First Image
        img = Image.open("images/admin_register_heading.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1 = Image.open("images/admin_register_heading.jpg")
        img1 = img1.resize((550, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=550, height=130)

        # Third Image
        img2 = Image.open("images/admin_register_heading.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # bg Image
        img3 = Image.open("images/blue-dark-gradient-texture-wall-background_28629-888.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="Student Management System", font=('lucida', 35, "bold"),
                          bg='green', fg='white')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left  label frame

        Left_frame = LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student Details',font=('lucida',12,'bold'))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img4= Image.open("images/blue-dark-gradient-texture-wall-background_28629-888.jpg")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(Left_frame, image=self.photoimg4)
        bg_img.place(x=5, y=0, width=720, height=130)

        #Current Course
        current_frame = LabelFrame(Left_frame, bd=2, bg='white', relief=RIDGE, text='Current Course Information',
                                font=('lucida', 12, 'bold'))
        current_frame.place(x=5, y=130, width=720, height=110)

        #Department
        dep_label = Label(current_frame,text="Department",bg='white',font=('lucida', 12, 'bold'))
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo = ttk.Combobox(current_frame,textvariable = self.var_dep,font=('lucida', 12, 'bold'),width = 17,state= 'readonly')
        dep_combo["values"]=('Select Department','CS','IT','Civil','Mechanical')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # Course
        course_label = Label(current_frame, text="Course", bg='white', font=('lucida', 12, 'bold'))
        course_label.grid(row=0, column=2, padx=10,sticky= W)

        course_combo = ttk.Combobox(current_frame,textvariable = self.var_course, font=('lucida', 12, 'bold'), width=17, state='readonly')
        course_combo["values"] = ('Select Course', 'FE', 'SE', 'TE', 'BE')
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)

        # Year
        year_label = Label(current_frame, text="Year", bg='white', font=('lucida', 12, 'bold'))
        year_label.grid(row=1, column=0, padx=10,sticky=W)

        year_combo = ttk.Combobox(current_frame,textvariable = self.var_year, font=('lucida', 12, 'bold'), width=17, state='readonly')
        year_combo["values"] = ('Select Year', '2020-21', '2021-22', '2022-23', '2023-24')
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10,sticky=W)

        # Semester
        semester_label = Label(current_frame, text="Semester", bg='white', font=('lucida', 12, 'bold'))
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_frame,textvariable = self.var_semester,font=('lucida', 12, 'bold'), width=17, state='readonly')
        semester_combo["values"] = ('Select Semester', 'Semester-1','Semester-2')
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg='white', relief=RIDGE, text='Class Student Information',
                                   font=('lucida', 12, 'bold'))
        class_Student_frame.place(x=5, y=250, width=720, height=300)

        #student ID
        studentID_lbl = Label(class_Student_frame,text="StudentID:", bg='white', font=('lucida', 12, 'bold'))
        studentID_lbl.grid(row=0, column=0, padx=10,pady=5 ,sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame,textvariable = self.var_stdID,width=20, font=('lucida', 12, 'bold'))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5 ,sticky=W)

        # student name
        studentName_lbl = Label(class_Student_frame, text="Student Name:", bg='white', font=('lucida', 12, 'bold'))
        studentName_lbl.grid(row=0, column=2, padx=10,pady=5 ,sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable = self.var_stdName, width=20, font=('lucida', 12, 'bold'))
        studentName_entry.grid(row=0, column=3, padx=10,pady=5 ,sticky=W)

        # class division
        class_div_lbl = Label(class_Student_frame, text="Class Division:", bg='white', font=('lucida', 12, 'bold'))
        class_div_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_div, font=('lucida', 12, 'bold'), width=18,state='readonly')
        div_combo["values"] = ('A', 'B', 'C', 'D')
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll NO
        rollno_lbl = Label(class_Student_frame, text="Roll no:", bg='white', font=('lucida', 12, 'bold'))
        rollno_lbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        rollno_entry = ttk.Entry(class_Student_frame,textvariable = self.var_roll, width=20, font=('lucida', 12, 'bold'))
        rollno_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        # gender
        gender_lbl = Label(class_Student_frame, text="Gender:", bg='white', font=('lucida', 12, 'bold'))
        gender_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender, font=('lucida', 12, 'bold'), width=18,state='readonly')
        gender_combo["values"] = ('Male','Female','other')
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # dob
        dob_lbl = Label(class_Student_frame, text="DOB:", bg='white', font=('lucida', 12, 'bold'))
        dob_lbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame,textvariable = self.var_dob, width=20, font=('lucida', 12, 'bold'))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)


        # email
        email_lbl = Label(class_Student_frame, text="Email:", bg='white', font=('lucida', 12, 'bold'))
        email_lbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame, width=20,textvariable = self.var_email, font=('lucida', 12, 'bold'))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        phone_lbl = Label(class_Student_frame, text="Phone No:", bg='white', font=('lucida', 12, 'bold'))
        phone_lbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame,textvariable = self.var_phone, width=20, font=('lucida', 12, 'bold'))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)


        # Address
        Address_lbl = Label(class_Student_frame, text="Address:", bg='white', font=('lucida', 12, 'bold'))
        Address_lbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        Address_entry = ttk.Entry(class_Student_frame,textvariable = self.var_address, width=20, font=('lucida', 12, 'bold'))
        Address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name
        teacher_name_lbl = Label(class_Student_frame, text="Teacher name:", bg='white', font=('lucida', 12, 'bold'))
        teacher_name_lbl.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_name_entry = ttk.Entry(class_Student_frame,textvariable = self.var_teacher, width=20, font=('lucida', 12, 'bold'))
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        #radio buttons
        self.var_radio1 = StringVar()
        radio1 = ttk.Radiobutton(class_Student_frame,variable = self.var_radio1,text='take photo sample',value="Yes")
        radio1.grid(row=5,column=0)

        radio2 = ttk.Radiobutton(class_Student_frame,variable = self.var_radio1, text='No photo sample', value="No")
        radio2.grid(row=5, column=1)

        #Button Frame
        btn_frame = Frame(class_Student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn = Button(btn_frame,text="Save",command= self.add_data,width=17,font=('lucida',13,'bold'),bg='blue',fg='white')
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",command=self.Update_data,width=17,font=('lucida',13,'bold'),bg='blue',fg='white')
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=17, font=('lucida', 13, 'bold'), bg='blue', fg='white')
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_Data,width=17, font=('lucida', 13, 'bold'), bg='blue', fg='white')
        reset_btn.grid(row=0, column=3)

       #Take Photo sample Btn frame
        btn1_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg='white')
        btn1_frame.place(x=0, y=235, width=715, height=35)

        take_photo_btn = Button(btn1_frame, text="Take Photo Sample", width=35,command= self.generate_dataset, font=('lucida', 13, 'bold'), bg='blue', fg='white')
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn1_frame, text="Update Photo Sample", width=35, font=('lucida', 13, 'bold'), bg='blue',  fg='white')
        update_photo_btn.grid(row=0, column=1)





        # right  label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text='Student Details',
                                 font=('lucida', 12, 'bold'))
        Right_frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open("images/city3.png")
        img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=0, y=0, width=720, height=130)


        #===========Search System =============================
        Search_frame = LabelFrame(Right_frame, bd=2, bg='white', relief=RIDGE, text='Search System',
                                font=('lucida', 12, 'bold'))
        Search_frame.place(x=5, y=135, width=710, height=70)

        search_lbl = Label(Search_frame, text="Search By:", bg='red', font=('lucida', 15, 'bold'),fg='white')
        search_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=('lucida', 12, 'bold'), width=17, state='readonly')
        search_combo["values"] = ('Select', 'Roll_No', 'PhoneNo')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=15, font=('lucida', 12, 'bold'))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Search", width=10, font=('lucida', 12, 'bold'), bg='blue',
                                fg='white')
        search_btn.grid(row=0, column=3,padx=4)

        showall = Button(Search_frame, text="Show All", width=12, font=('lucida', 12, 'bold'),
                                  bg='blue', fg='white')
        showall.grid(row=0, column=4,padx=4)


        #=======================Table Frame ==============================
        Table_frame = Frame(Right_frame, bd=2, bg='white', relief=RIDGE)
        Table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', background='white', font=('Arial', 12), foreground='black', rowheight=28,
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', 'green')])
        self.student_table = ttk.Treeview(Table_frame, columns=(
            'dep', 'course', 'year', 'sem', 'id', 'name', 'div','roll','gender','dob','email','phone', 'address','teacher','photo'),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Rollno")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo")

        self.student_table['show'] = "headings"
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #====================== Function Declaration ======================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_stdName.get() == "" or self.var_stdID.get() == "":
            tsmg.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",username="root",password='root@amit',database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_stdID.get(),
                                                                                                        self.var_stdName.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                tsmg.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                tsmg.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #=========================== Fetch data ===========================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password='root@amit',database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute('select * from student')
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data :
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=============== get cursor =========================
    def get_cursor(self,event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_stdID.set(data[4]),
        self.var_stdName.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #========== update functions =========
    def Update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_stdName.get() == "" or self.var_stdID.get() == "":
            tsmg.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update = tsmg.askyesno("Update",'Do you want to update this student details',parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password='root@amit',database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute('update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s',(
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_stdName.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_stdID.get()
                                                                                                                                                                                                    ))
                else:
                    if  not update:
                        return
                tsmg.showinfo("Success","Student details Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                tsmg.showerror("Error",f"Due to {str(es)}",parent=self.root)

    #=========== Delete=============================
    def delete_data(self):
        if self.var_stdID.get()=="":
            tsmg.showerror("Error","Student ID must bre required",parent=self.root)
        else:
            try:
                delete = tsmg.askyesno("Update", 'Do you want to delete this student details', parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password='root@amit',database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_stdID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                tsmg.showinfo("Delete","Successfully Deleted Studnet details",parent=self.root)
            except Exception as es:
                tsmg.showerror("Error", f"Due to {str(es)}", parent=self.root)

    #====== reset
    def reset_Data(self):
        self.var_dep.set('Select Department'),
        self.var_course.set('Select Course'),
        self.var_year.set('Select Year'),
        self.var_semester.set('Select Semester'),
        self.var_stdID.set(""),
        self.var_stdName.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    #=================== Generate Dataset and take photo sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_stdName.get() == "" or self.var_stdID.get() == "":
            tsmg.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password='root@amit',database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute('select * from student')
                myresult = my_cursor.fetchall()
                id  = 0
                for x in myresult:
                    id +=1
                my_cursor.execute(
                'update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s',
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_stdName.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_stdID.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_Data()
                conn.close()

                #============ Load predefined data on face frontals from opencv==============
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor=1.3
                    #Minimum Neighbours = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None :
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path ="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 20)
                        cv2.imshow("Cropped Face",face)


                    if cv2.waitKey(1) ==13 or int(img_id) == 70:
                        break
                cap.release()

                cv2.destroyAllWindows()
                tsmg.showinfo("Result","Generating datasets Completed",parent=self.root)

            except Exception as es:
                tsmg.showerror("Error",f"Due to:{str(es)}",parent=self.root)

if __name__ == "__main__":
    root =Tk()
    obj = Student(root)
    root.mainloop()
