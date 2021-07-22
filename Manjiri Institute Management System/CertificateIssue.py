import pymysql
from tkinter import *
from tkinter import ttk, messagebox

class Certificate:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1000x480+0+160")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="Certificate Issue Form", font=("goudy old style", 20, "bold"), bg="orange",fg="#262626").place(x=0,y=0,width=1000,height=35)

        #===============Variables===============================
        self.var_batch=StringVar()
        self.var_rname=StringVar()
        self.var_course=StringVar()
        self.var_CertificateNo = StringVar()
        self.var_Certificate_issue=StringVar()
        self.var_C_issue_date=StringVar()
        self.var_Marksheet_issue=StringVar()
        self.var_M_issue_date=StringVar()
        self.var_remark=StringVar()



        #====Labels=============================================
        lbl_Batch = Label(self.root, text="Batch", font=("goudy old style", 15, "bold"), bg="white").place(x=20, y=60)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=20, y=100)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=20,
                                                                                                             y=140)
        lbl_CertificateNo = Label(self.root, text="Certificate No.", font=("goudy old style", 15, "bold"), bg="white").place(
            x=20, y=180)
        lbl_Certificate_issue = Label(self.root, text="Certificate Issued", font=("goudy old style", 15, "bold"), bg="white").place(x=20,
                                                                                                                  y=220)
        lbl_C_issue_date= Label(self.root, text="Issue Date", font=("goudy old style", 15, "bold"), bg="white").place(x=20,y=260)
        lbl_Markshheet_issue= Label(self.root, text="Marksheet Issued", font=("goudy old style", 15, "bold"), bg="white").place(x=20,y=300)
        lbl_M_issue_date = Label(self.root, text="Issue Date", font=("goudy old style", 15, "bold"), bg="white").place(x=20, y=340)
        lbl_remark = Label(self.root, text="Remark", font=("goudy old style", 15, "bold"), bg="white").place(x=20,y=380)


        #===============Entry fields=====================
        self.course_list = ["Select "]

        # Function call to update course list
        self.fetch_course()
        self.txt_batch = ttk.Combobox(self.root, textvariable=self.var_batch,
                                      values=("Select", "January", "February", "March", "April", "May", "June", "July",
                                              "August", "September", "October", 'November', "December"),
                                      font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_batch.place(x=220, y=60,width=203)
        self.txt_batch.current(0)
        txt_name = Entry(self.root, textvariable=self.var_rname, font=("goudy old style", 15, "bold"), bg="light yellow").place(x=220, y=100)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list,
                                       font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_course.place(x=220, y=140, width=203)
        self.txt_course.current(0)
        txt_CertificateNo = Entry(self.root, textvariable=self.var_CertificateNo, font=("goudy old style", 15, "bold"), bg="light yellow").place(x=220, y=180)
        txt_Certificate_issue = Entry(self.root, textvariable=self.var_Certificate_issue, font=("goudy old style", 15, "bold"), bg="light yellow").place(x=220,y=220)
        txt_C_issue_date= Entry(self.root, textvariable=self.var_C_issue_date, font=("goudy old style", 15, "bold"), bg="light yellow").place(x=220,y=260)
        txt_Markshheet_issue= Entry(self.root, textvariable=self.var_Marksheet_issue, font=("goudy old style", 15, "bold"), bg="light yellow").place(x=220,y=300)
        txt_M_issue_date = Entry(self.root, textvariable=self.var_M_issue_date, font=("goudy old style", 15, "bold"), bg="light yellow").place(x=220, y=340)
        txt_remark = Entry(self.root, textvariable=self.var_remark, font=("goudy old style", 15, "bold"), bg="light yellow").place(x=220,y=380)

        #=========Buttons========================================
        self.btn_add = Button(self.root, text="Submit", font=("goudy old style", 15, "bold"),bg="#2196f3", fg="white", cursor="hand2",command=self.add)
        self.btn_add.place(x=50, y=420, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"),bg="violet", fg="white", cursor="hand2",command=self.update)
        self.btn_update.place(x=175, y=420, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"),bg="#6078db", fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=300, y=420, width=110, height=40)

        #================DatabaseFrame==============================
        #===============Buttons=====================================
        self.btn_R_table = Button(self.root, text="Registration Table", font=("goudy old style", 13, "bold"),

                                  bg="#6078db", fg="white", cursor="hand2",command=self.Register_table)
        self.btn_R_table.place(x=550, y=50, width=135, height=28)

        self.btn_C_table = Button(self.root, text="Certificate Issue Table", font=("goudy old style", 13, "bold"),
                                  bg="#6078db", fg="white", cursor="hand2",command=self.Certificate_Table)
        self.btn_C_table.place(x=730, y=50, width=155, height=28)
        btn_X = Button(self.root, text="X", font=("goudy old style", 18, "bold"), bg="white", bd=1, fg="red",
                       cursor="hand2",command=self.blank_frame).place(x=940, y=50, width=30, height=25)

        # ==============Registration  table ==============================================
    def Register_table(self):
        self.C_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.C_frame.place(x=450, y=82, width=540, height=389)

        # =============Search Panel==================
        self.var_Search = StringVar()

        lbl_search_search_regid = Label(self.C_frame, text="Search by|Name ", font=("goudy old style", 15, "bold"),bg="white").place(x=40, y=10)
        self.txt_search_studentname = Entry(self.C_frame, textvariable=self.var_Search,font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_search_studentname.place(x=200, y=10, width=180)

        btn_Search = Button(self.C_frame, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4",fg="white",cursor="hand2",command=self.r_search).place(x=400, y=10, width=110, height=28)

        # ==========Content ============

        lbl_registration_table = Label(self.C_frame, text="Registration table",font=("goudy old style", 15, "bold"),bg="white").place(x=220, y=40)

        self.D_frame = Frame(self.C_frame, bg="white")
        self.D_frame.place(x=0, y=70, width=540, height=319)
        scroll_x = Scrollbar(self.D_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.D_frame, orient=VERTICAL)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', background='white', font=('Arial', 12), foreground='black', rowheight=28,
                            fieldbackground='white')
        style.map('Treeview', background=[('selected', 'green')])
        self.RegisterTable = ttk.Treeview(self.D_frame, columns=(
                'regid', 'batch', 'name','course',),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.RegisterTable.xview)
        scroll_y.config(command=self.RegisterTable.yview)

        self.RegisterTable.heading("regid", text="REG ID")
        self.RegisterTable.heading("batch", text="Batch")
        self.RegisterTable.heading("name", text="Name")
        self.RegisterTable.heading("course", text="Course")

        self.RegisterTable['show'] = "headings"
        self.RegisterTable.column("regid", width=150)
        self.RegisterTable.column("batch", width=150)
        self.RegisterTable.column("name", width=150)
        self.RegisterTable.column("course", width=150)
        self.RegisterTable.pack(fill=BOTH, expand=1)
        self.RegisterTable.bind('<ButtonRelease-1>', self.get_data)
        self.show()

    #===================Certificate Issue Table==========================================================
    def Certificate_Table(self):
        self.Certificate_table_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.Certificate_table_frame.place(x=450, y=82, width=540, height=389)

        # =============Search Panel==================
        self.c_var_Search = StringVar()

        lbl_search_search_regid = Label(self.Certificate_table_frame, text="Search by|Name ", font=("goudy old style", 15, "bold"),
                                        bg="white").place(x=40, y=10)
        self.txt_search_certificate = Entry(self.Certificate_table_frame, textvariable=self.c_var_Search,
                                           font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_search_certificate.place(x=200, y=10, width=180)

        btn_Search = Button(self.Certificate_table_frame, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",
                            cursor="hand2",command=self.c_search).place(x=400, y=10, width=110, height=28)

        # ==========Content ============

        lbl_Certificate_table = Label(self.Certificate_table_frame, text="Certificate Issue Table", font=("goudy old style", 15, "bold"),
                                       bg="white").place(x=220, y=40)

        self.Database_frame = Frame(self.Certificate_table_frame, bg="white")
        self.Database_frame.place(x=0, y=70, width=540, height=319)
        scroll_x = Scrollbar(self.Database_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.Database_frame, orient=VERTICAL)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', background='white', font=('Arial', 12), foreground='black', rowheight=28,
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', 'green')])
        self.Certificate_table = ttk.Treeview(self.Database_frame, columns=(
            'batch', 'name', 'course', 'certificateno','certificateissue','cissuedate','marksheetissue','missuedate','remark',), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Certificate_table.xview)
        scroll_y.config(command=self.Certificate_table.yview)

        self.Certificate_table.heading("batch", text="Batch")
        self.Certificate_table.heading("name", text="Name")
        self.Certificate_table.heading("course", text="Course")
        self.Certificate_table.heading("certificateno", text="Certificate No.")
        self.Certificate_table.heading("certificateissue", text="Certificate Issued")
        self.Certificate_table.heading("cissuedate", text="Certificate Issue Date")
        self.Certificate_table.heading("marksheetissue", text="Marksheet Issued")
        self.Certificate_table.heading("missuedate", text="Marksheet Issue Date")
        self.Certificate_table.heading("remark", text="Remark")

        self.Certificate_table['show'] = "headings"
        self.Certificate_table.column("batch", width=150)
        self.Certificate_table.column("name",width=150)
        self.Certificate_table.column("course",width=150)
        self.Certificate_table.column("certificateno",width=150)
        self.Certificate_table.column("certificateissue", width=150)
        self.Certificate_table.column("cissuedate",width=150)
        self.Certificate_table.column("marksheetissue",width=150)
        self.Certificate_table.column("missuedate",width=150)
        self.Certificate_table.column("remark",width=150)
        self.Certificate_table.pack(fill=BOTH, expand=1)
        self.Certificate_table.bind('<ButtonRelease-1>', self.c_get_data)
        self.c_show()



    #=======================================================================================================
    def get_data(self, event):
        # self.txt_regid.config(state="readonly")
        r = self.RegisterTable.focus()
        content = self.RegisterTable.item(r)
        row = content["values"]
        self.var_batch.set(row[1]),
        self.var_rname.set(row[2])
        self.var_course.set(row[3])

    def c_get_data(self, event):
        # self.txt_regid.config(state="readonly")
        r = self.Certificate_table.focus()
        content = self.Certificate_table.item(r)
        row = content["values"]
        self.var_batch.set(row[0]),
        self.var_rname.set(row[1])
        self.var_course.set(row[2])
        self.var_CertificateNo.set(row[3])
        self.var_Certificate_issue.set(row[4])
        self.var_C_issue_date.set(row[5])
        self.var_Marksheet_issue.set(row[6])
        self.var_M_issue_date.set(row[7])
        self.var_remark.set(row[8])

    def c_show(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select * from certificate_table")
            rows = cur.fetchall()
            self.Certificate_table.delete(*self.Certificate_table.get_children())
            for row in rows:
                self.Certificate_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def show(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select regid,batch,name,course from register_student")
            rows = cur.fetchall()
            self.RegisterTable.delete(*self.RegisterTable.get_children())
            for row in rows:
                self.RegisterTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def add(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        try:
            if self.var_rname.get() == "":
                messagebox.showerror("Error", "Student Name should be required", parent=self.root)
            else:
                cur.execute('select * from certificate_table where name =%s', (self.var_rname.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Name is already present", parent=self.root)
                else:
                    cur.execute(
                        "insert into certificate_table(batch,name,course,certificateno,certificateissue,cissuedate,marksheetissue,missuedate,remark) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_batch.get(),
                            self.var_rname.get(),
                            self.var_course.get(),
                            self.var_CertificateNo.get(),
                            self.var_Certificate_issue.get(),
                            self.var_C_issue_date.get(),
                            self.var_Marksheet_issue.get(),
                            self.var_M_issue_date.get(),
                            self.var_remark.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Student added successfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def update(self):

        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        try:
            if self.var_rname.get() == "":
                messagebox.showerror("Error", "Name should be required", parent=self.root)
            else:
                cur.execute('select * from certificate_table where name=%s', (self.var_rname.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Student from list", parent=self.root)
                else:

                    cur.execute(
                        "update certificate_table set batch=%s,course=%s,certificateno=%s,certificateissue=%s,cissuedate=%s,marksheetissue=%s,missuedate=%s,remark=%s where name=%s",
                        (
                            self.var_batch.get(),
                            self.var_course.get(),
                            self.var_CertificateNo.get(),
                            self.var_Certificate_issue.get(),
                            self.var_C_issue_date.get(),
                            self.var_Marksheet_issue.get(),
                            self.var_M_issue_date.get(),
                            self.var_remark.get(),
                            self.var_rname.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Student Updated successfully", parent=self.root)
                    self.c_show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def clear(self):
        self.var_batch.set("Select")
        self.var_rname.set("")
        self.var_course.set("Select")
        self.var_CertificateNo.set("")
        self.var_Certificate_issue.set("")
        self.var_C_issue_date.set("")
        self.var_Marksheet_issue.set("")
        self.var_M_issue_date.set("")
        self.var_remark.set("")
        self.txt_search_certificate.delete(0,END)


    def r_search(self):
        if self.txt_search_studentname.get() == "":
            messagebox.showerror("Error", "Please enter Student  name", parent=self.root)
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select regid,batch,name,course from register_student where name=%s", (self.var_Search.get(),))
            row = cur.fetchone()
            if row != None:
                self.RegisterTable.delete(*self.RegisterTable.get_children())
                self.RegisterTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        self.var_Search.set("")


    def c_search(self):
        if self.txt_search_certificate.get() == "":
            messagebox.showerror("Error", "Please enter Student  name", parent=self.root)
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select * from certificate_table where name=%s", (self.c_var_Search.get(),))
            row = cur.fetchone()
            if row != None:
                self.Certificate_table.delete(*self.Certificate_table.get_children())
                self.Certificate_table.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        self.var_Search.set("")


    def blank_frame(self):
        self.f = Frame(self.root,bg='white')
        self.f.place(x=450, y=82, width=540, height=389)

    def fetch_course(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Certificate(root)
    root.mainloop()