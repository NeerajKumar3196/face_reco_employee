from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x695+0+0")
        self.root.title("Employee's Attendance Face Recognition System")


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

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Developer","IT Sales","Architect","System Engineer")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

    # Doj

        join_label=Label(current_course_frame,text="Year Of Joining",font=("times new roman",12,"bold"),bg="white")
        join_label.grid(row=0,column=2,padx=10, sticky=W)

        join_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        join_combo["values"]=("Select Year","2017","2018","2019","2020")
        join_combo.current(0)
        join_combo.grid(row=0,column=3,padx=2,pady=10, sticky=W)


    #Location

        loc_label=Label(current_course_frame,text="Current Location",font=("times new roman",12,"bold"),bg="white")
        loc_label.grid(row=1,column=0,padx=10, sticky=W)

        loc_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        loc_combo["values"]=("Select Location","Bangalore","Pune","Hydeabad","Chennai")
        loc_combo.current(0)
        loc_combo.grid(row=1,column=1,padx=2,pady=10, sticky=W)


    # Employee information

        emp_inf_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Employee Information",font=("times new roman",12,"bold"))
        emp_inf_frame.place(x=5,y=250,width=745,height=290)

    #EMmp id

        emp_id_label=Label(emp_inf_frame,text="Employee Id",font=("times new roman",12,"bold"),bg="white")
        emp_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        emp_id_entry=ttk.Entry(emp_inf_frame,width=20,font=("times new roman",12,"bold"))
        emp_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


    #Emp name

        emp_nm_label=Label(emp_inf_frame,text="Employee Name",font=("times new roman",12,"bold"),bg="white")
        emp_nm_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        emp_nm_entry=ttk.Entry(emp_inf_frame,width=20,font=("times new roman",12,"bold"))
        emp_nm_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

    #Emp Gender

        gender_label=Label(emp_inf_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(emp_inf_frame,width=20,font=("times new roman",12,"bold"))
        gender_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

    #Emp DOB

        dob_label=Label(emp_inf_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(emp_inf_frame,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

    #Emp Email

        Email_label=Label(emp_inf_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(emp_inf_frame,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

    #Emp contact

        phone_label=Label(emp_inf_frame,text="Phone Number",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(emp_inf_frame,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)



    #Emp add

        add_label=Label(emp_inf_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        add_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        add_entry=ttk.Entry(emp_inf_frame,width=20,font=("times new roman",12,"bold"))
        add_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

    #radio button

        radiobtn1=ttk.Radiobutton(emp_inf_frame,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=4,column=0)

        radiobtn2=ttk.Radiobutton(emp_inf_frame,text="No Photo Sample", value="No")
        radiobtn2.grid(row=4,column=1)

    #btn frame
        btn_frame=LabelFrame(emp_inf_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=170,width=730,height=90)

        save_btn=Button(btn_frame,text="Save",width=15,font=("times new roman",16,"bold"),bg="sky blue",fg="dark Green")
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

        self.emp_table=ttk.Treeview(Table_frame,column=("job title","yoj","loc","id","emp name","gender","dob","email","phone","add","photo"))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.emp_table.xview)
        scroll_y.config(command=self.emp_table.yview)

        self.emp_table.heading("job title",text="Job Title")
        self.emp_table.heading("yoj",text="Year Of Joining")
        self.emp_table.heading("loc",text="Current Location")
        self.emp_table.heading("id",text="Employee Id")
        self.emp_table.heading("emp name",text="Employee Name")
        self.emp_table.heading("gender",text="Gender")
        self.emp_table.heading("dob",text="DOB")
        self.emp_table.heading("email",text="Email")
        self.emp_table.heading("phone",text="Phone Number")
        self.emp_table.heading("add",text="Address")
        self.emp_table.heading("photo",text="PhotoSampleStatus")

        self.emp_table["show"]="headings"

       

        
        # self.emp_table.column("job title",width=100)
        # self.emp_table.column("yoj",width=100)
        # self.emp_table.column("loc",width=100)
        # self.emp_table.column("id",width=100)
        # self.emp_table.column("emp name",width=100)
        # self.emp_table.column("gender",width=100)
        # self.emp_table.column("dob",width=100)
        # self.emp_table.column("email",width=100)
        # self.emp_table.column("phone",width=100)
        # self.emp_table.column("add",width=100)
        # self.emp_table.column("photo",width=100)
        
        self.emp_table.pack(fill=BOTH,expand=1)



       

if __name__ == "__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
