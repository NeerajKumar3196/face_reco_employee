from textwrap import fill
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from PIL import Image,ImageTk
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1400x695+0+0")
                self.root.title("Employee's Attendance Face Recognition System")


                #=============== variables ================
                self.var_atten_id=StringVar()
                self.var_atten_name=StringVar()
                self.var_atten_title=StringVar()
                self.var_atten_phone_number=StringVar()
                self.var_atten_time=StringVar()
                self.var_atten_date=StringVar()
                self.var_atten_attendance=StringVar()

                # bg_image 

                img=Image.open(r"D:\face_rekog_employee\face_reco_employee\images\face1.png")
                img=img.resize((1500,695),Image.ANTIALIAS)
                self.photoimg=ImageTk.PhotoImage(img)

                bg_img=Label(self.root,image=self.photoimg)
                bg_img.place(x=0,y=0,width=1500,height=695)

                #=====title 

                title_lbl =Label(bg_img,text="Attendance Management System",font=("times new Roman",35,"bold"),bg="blue",fg="white")
                title_lbl.place(x=0,y=0,width=1450,height=55)

                main_frame=Frame(bg_img,bd=2)
                main_frame.place(x=20,y=65,width=1310,height=620)

                #left label frame

                Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee information ",font=("times new roman",12,"bold"))
                Left_frame.place(x=10,y=10,width=610,height=580)

                img_left=Image.open(r"D:\face_rekog_employee\face_reco_employee\images\employees.jpg")
                img_left=img_left.resize((500,120),Image.ANTIALIAS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                left_img=Label(Left_frame,image=self.photoimg_left)
                left_img.place(x=5,y=0,width=550,height=120)

                left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
                left_inside_frame.place(x=5,y=180,width=600,height=400)


                # label and entry
                # ==== employee id =====
                emp_id_label=Label(left_inside_frame,text="Employee Id",font=("times new roman",12,"bold"),bg="white")
                emp_id_label.grid(row=0,column=0,padx=4,pady=5,sticky=W)

                emp_id_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
                emp_id_entry.grid(row=0,column=1,padx=4,pady=5,sticky=W)

                # ==== Name =====
                name_label=Label(left_inside_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
                name_label.grid(row=0,column=2,padx=4,pady=5,sticky=W)

                name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
                name_entry.grid(row=0,column=3,padx=4,pady=5,sticky=W)

                # ==== department =====
                date_label=Label(left_inside_frame,text="Title",font=("times new roman",12,"bold"),bg="white")
                date_label.grid(row=1,column=0,padx=4,pady=5,sticky=W)

                date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_title,font=("times new roman",12,"bold"))
                date_entry.grid(row=1,column=1,padx=4,pady=5,sticky=W)

                # ==== phone number=====
                dep_label=Label(left_inside_frame,text="Phone number",font=("times new roman",12,"bold"),bg="white")
                dep_label.grid(row=1,column=2,padx=4,pady=5,sticky=W)

                dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_phone_number,font=("times new roman",12,"bold"))
                dep_entry.grid(row=1,column=3,padx=4,pady=5,sticky=W)

                # ==== time =====
                time_label=Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
                time_label.grid(row=2,column=0,padx=4,pady=5,sticky=W)

                time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
                time_entry.grid(row=2,column=1,padx=4,pady=5,sticky=W)

                # ==== date =====
                time_label=Label(left_inside_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
                time_label.grid(row=2,column=2,padx=4,pady=5,sticky=W)

                time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
                time_entry.grid(row=2,column=3,padx=4,pady=5,sticky=W)


                # ==== attendance  =====
                attendance_label=Label(left_inside_frame,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
                attendance_label.grid(row=3,column=0,padx=4,pady=5,sticky=W)

                self.atten_status=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
                self.atten_status["values"]=("Status","Present","Absent")
                self.atten_status.current(0)
                self.atten_status.grid(row=3,column=1,padx=4,pady=5, sticky=W)


                #btn frame
                btn_frame=LabelFrame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=5,y=300,width=730,height=45)

                imp_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=12,font=("times new roman",16,"bold"),bg="sky blue",fg="dark Green")
                imp_btn.grid(row=0,column=0)

                exp_btn=Button(btn_frame,text="Export Csv",width=12,command=self.exportCsv,font=("times new roman",16,"bold"),bg="blue",fg="Yellow")
                exp_btn.grid(row=0,column=1)

                upd_btn=Button(btn_frame,text="Update",width=12,font=("times new roman",16,"bold"),bg="sky blue",fg="red")
                upd_btn.grid(row=0,column=2)

                reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("times new roman",16,"bold"),bg="blue",fg="Orange")
                reset_btn.grid(row=0,column=3)


                

        #==========   right label frame

                Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
                Right_frame.place(x=630,y=10,width=670,height=580)

                table_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,bg="white")
                table_frame.place(x=5,y=5,width=650,height=455)

        # =====  scroll bar =========================
                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","name","title","phone_number","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.AttendanceReportTable.xview)
                scroll_y.config(command=self.AttendanceReportTable.yview)

                self.AttendanceReportTable.heading("id",text="Attendance ID")
                self.AttendanceReportTable.heading("name",text="Name")
                self.AttendanceReportTable.heading("title",text="job_title")
                self.AttendanceReportTable.heading("phone_number",text="Phone_number")
                self.AttendanceReportTable.heading("time",text="Time")
                self.AttendanceReportTable.heading("date",text="Date")
                self.AttendanceReportTable.heading("attendance",text="Attendance Status")

                self.AttendanceReportTable["show"]="headings"

                self.AttendanceReportTable.column("id",width=120)
                self.AttendanceReportTable.column("name",width=120)
                self.AttendanceReportTable.column("title",width=120)
                self.AttendanceReportTable.column("phone_number",width=120)
                self.AttendanceReportTable.column("time",width=120)
                self.AttendanceReportTable.column("date",width=120)
                self.AttendanceReportTable.column("attendance",width=120)



                self.AttendanceReportTable.pack(fill=BOTH,expand=1)

                self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


        # ================== Fetch data ===================


        def fetchData(self,rows):
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in rows:
                        self.AttendanceReportTable.insert("",END,values=i)

        
        def importCsv(self):
                global mydata
                mydata.clear()
                fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
                with open (fln) as myfile:
                        csvread=csv.reader(myfile,delimiter=",")
                        for i in csvread:
                                mydata.append(i)
                        self.fetchData(mydata)

        def exportCsv(self):
                try:
                        if len(mydata)<1:
                                messagebox.showerror("No Data"," no data found to export",parent=self.root)
                                return False
                        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
                        with open(fln,mode="w",newline="") as myfile:
                                exp_write=csv.writer(myfile,delimiter=",")
                                for i in mydata:
                                        exp_write.writerow(i)
                                messagebox.showinfo("Data Export","your data exported"+os.path.basename(fln)+ "successfully")


                except Exception as es:
                        messagebox.showerror("error",f"due to:{ str(es)}",parent=self.root)

        def get_cursor(self,event=""):
                cursor_row=self.AttendanceReportTable.focus()
                content=self.AttendanceReportTable.item(cursor_row)
                rows=content['values']
                self.var_atten_id.set(rows[0])
                self.var_atten_name.set(rows[1])
                self.var_atten_title.set(rows[2])
                self.var_atten_phone_number.set(rows[3])
                self.var_atten_time.set(rows[4])
                self.var_atten_date.set(rows[5])
                self.var_atten_attendance.set(rows[6])

        def reset_data(self):
                self.var_atten_id.set("")
                self.var_atten_name.set("")
                self.var_atten_title.set("")
                self.var_atten_phone_number.set("")
                self.var_atten_time.set("")
                self.var_atten_date.set("")
                self.var_atten_attendance.set("")




if __name__ == "__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop()