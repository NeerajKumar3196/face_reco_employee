from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x695+0+0")
        self.root.title("Employee's Attendance Face Recognition System")

    #======variables===============================
        
        self.var_title=StringVar()
        self.var_yoj=StringVar()
        self.var_loc=StringVar()
        self.var_id=StringVar()
        self.var_emp_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_add=StringVar()



    #bg image

        img=Image.open(r"D:\face_rekog_employee\face_reco_employee\images\bg4.jpg")
        img=img.resize((1400,695),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=695)

    #title

        title_lbl =Label(bg_img,text="Employee's Management System",font=("times new Roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1400,height=55)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=65,width=1310,height=620)

    #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)

        img_left=Image.open(r"D:\face_rekog_employee\face_reco_employee\images\employees.jpg")
        img_left=img_left.resize((500,120),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        left_img=Label(Left_frame,image=self.photoimg_left)
        left_img.place(x=5,y=0,width=700,height=120)

    # current details
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current profile",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=125,width=745,height=120)

    # job Title 
        dep_label=Label(current_course_frame,text="Job Title",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_title,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Developer","IT Sales","Architect","System Engineer")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

    # Doj

        join_label=Label(current_course_frame,text="Year Of Joining",font=("times new roman",12,"bold"),bg="white")
        join_label.grid(row=0,column=2,padx=10, sticky=W)

        join_combo=ttk.Combobox(current_course_frame,textvariable=self.var_yoj,font=("times new roman",12,"bold"),state="readonly")
        join_combo["values"]=("Select Year","2017","2018","2019","2020")
        join_combo.current(0)
        join_combo.grid(row=0,column=3,padx=2,pady=10, sticky=W)


    #Location

        loc_label=Label(current_course_frame,text="Current Location",font=("times new roman",12,"bold"),bg="white")
        loc_label.grid(row=1,column=0,padx=10, sticky=W)

        loc_combo=ttk.Combobox(current_course_frame,textvariable=self.var_loc,font=("times new roman",12,"bold"),state="readonly")
        loc_combo["values"]=("Select Location","Bangalore","Pune","Hydeabad","Chennai")
        loc_combo.current(0)
        loc_combo.grid(row=1,column=1,padx=2,pady=10, sticky=W)


    # ==============Employee information=====

        emp_inf_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Employee Information",font=("times new roman",12,"bold"))
        emp_inf_frame.place(x=5,y=250,width=745,height=290)

    #EMmp id

        emp_id_label=Label(emp_inf_frame,text="Employee Id",font=("times new roman",12,"bold"),bg="white")
        emp_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        emp_id_entry=ttk.Entry(emp_inf_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        emp_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


    #Emp name

        emp_nm_label=Label(emp_inf_frame,text="Employee Name",font=("times new roman",12,"bold"),bg="white")
        emp_nm_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        emp_nm_entry=ttk.Entry(emp_inf_frame,textvariable=self.var_emp_name,width=20,font=("times new roman",12,"bold"))
        emp_nm_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

    #Emp Gender

        gender_label=Label(emp_inf_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(emp_inf_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        gender_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

    #Emp DOB

        dob_label=Label(emp_inf_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(emp_inf_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

    #Emp Email

        Email_label=Label(emp_inf_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(emp_inf_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

    #Emp contact

        phone_label=Label(emp_inf_frame,text="Phone Number",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(emp_inf_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)



    #Emp add

        add_label=Label(emp_inf_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        add_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        add_entry=ttk.Entry(emp_inf_frame,textvariable=self.var_add,width=20,font=("times new roman",12,"bold"))
        add_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

    #=============radio button=====

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(emp_inf_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=4,column=0)

        
        radiobtn2=ttk.Radiobutton(emp_inf_frame,variable=self.var_radio1,text="No Photo Sample", value="No")
        radiobtn2.grid(row=4,column=1)

    #btn frame
        btn_frame=LabelFrame(emp_inf_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=170,width=730,height=90)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",16,"bold"),bg="sky blue",fg="dark Green")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",16,"bold"),bg="blue",fg="Yellow")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=15,font=("times new roman",16,"bold"),bg="sky blue",fg="red")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=15,font=("times new roman",16,"bold"),bg="blue",fg="Orange")
        reset_btn.grid(row=0,column=3)


        btn_frame1=LabelFrame(emp_inf_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=210,width=730,height=45)

        Take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=30,font=("times new roman",16,"bold"),bg="sky blue",fg="Dark green")
        Take_photo_btn.grid(row=0,column=0)

        Update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=30,font=("times new roman",16,"bold"),bg="blue",fg="Orange")
        Update_photo_btn.grid(row=0,column=1)

    






    #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=520,height=580)


        img_Right=Image.open(r"D:\face_rekog_employee\face_reco_employee\images\employees.jpg")
        img_Right=img_Right.resize((500,120),Image.ANTIALIAS)
        self.photoimg_Right=ImageTk.PhotoImage(img_Right)

        Right_img=Label(Right_frame,image=self.photoimg_Right)
        Right_img.place(x=5,y=0,width=500,height=120)



    #======= Search System=============

        Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=125,width=505,height=90)

        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="white",fg="blue")
        Search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        Search_combo["values"]=("Select","Emp_id","Phone Number")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10, sticky=W)

        Search_entry=ttk.Entry(Search_frame,width=12,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)


        Search_btn=Button(Search_frame,text="Search",width=8,font=("times new roman",10,"bold"),bg="blue",fg="Yellow")
        Search_btn.grid(row=0,column=3)

        ShowAll_btn=Button(Search_frame,text="Show All",width=8,font=("times new roman",10,"bold"),bg="sky blue",fg="red")
        ShowAll_btn.grid(row=0,column=4)

    #==========Table Frame================


        Table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        Table_frame.place(x=5,y=225,width=505,height=320)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.emp_table=ttk.Treeview(Table_frame,column=("title","yoj","loc","id","emp_name","gender","dob","email","phone","add","photo"))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.emp_table.xview)
        scroll_y.config(command=self.emp_table.yview)

        self.emp_table.heading("title",text="Job Title")
        self.emp_table.heading("yoj",text="Year Of Joining")
        self.emp_table.heading("loc",text="Current Location")
        self.emp_table.heading("id",text="Employee Id")
        self.emp_table.heading("emp_name",text="Employee Name")
        self.emp_table.heading("gender",text="Gender")
        self.emp_table.heading("dob",text="DOB")
        self.emp_table.heading("email",text="Email")
        self.emp_table.heading("phone",text="Phone Number")
        self.emp_table.heading("add",text="Address")
        self.emp_table.heading("photo",text="PhotoSampleStatus")
        
        self.emp_table["show"]="headings"

       

        
        self.emp_table.column("title",width=150)
        self.emp_table.column("yoj",width=150)
        self.emp_table.column("loc",width=150)
        self.emp_table.column("id",width=150)
        self.emp_table.column("emp_name",width=150)
        self.emp_table.column("gender",width=150)
        self.emp_table.column("dob",width=150)
        self.emp_table.column("email",width=150)
        self.emp_table.column("phone",width=150)
        self.emp_table.column("add",width=150)
        self.emp_table.column("photo",width=150)
        
        self.emp_table.pack(fill=BOTH,expand=1)
        

        self.fetch_data()
#------------function  declaration==========

    def add_data(self):
        if self.var_title.get()=="Select Department" or self.var_emp_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                        self.var_title.get(),
                                                        self.var_yoj.get(),
                                                        self.var_loc.get(),
                                                        self.var_id.get(),
                                                        self.var_emp_name.get(),
                                                        self.var_gender.get(),
                                                        self.var_dob.get(),
                                                        self.var_email.get(),
                                                        self.var_phone.get(),
                                                        self.var_add.get(),
                                                        self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS","Employee details has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"due to :{str(es)}",parent=self.root)


    #====== fetch data =====
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from employee")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.emp_table.delete(*self.emp_table.get_children())
            for i in data:
                self.emp_table.insert("",END,values=i)
            conn.commit()
        conn.close()



if __name__ == "__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
