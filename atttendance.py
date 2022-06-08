from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2


class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x695+0+0")
        self.root.title("Employee's Attendance Face Recognition System")

          # bg_image 

        img=Image.open(r"D:\face_rekog_employee\face_reco_employee\images\face1.png")
        img=img.resize((1500,695),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1500,height=695)

#          title 

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
        left_inside_frame.place(x=5,y=125,width=590,height=300)


        # label and entry
        # ==== attendance id =====
        att_id_label=Label(left_inside_frame,text="Attendance Id",font=("times new roman",12,"bold"),bg="white")
        att_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        emp_id_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        emp_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # ==== Name =====
        att_id_label=Label(left_inside_frame,text="Attendance Id",font=("times new roman",12,"bold"),bg="white")
        att_id_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        emp_id_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        emp_id_entry.grid(row=0,column=3,padx=4,pady=8,sticky=W)

        # ==== date =====
        att_id_label=Label(left_inside_frame,text="Attendance Id",font=("times new roman",12,"bold"),bg="white")
        att_id_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        emp_id_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        emp_id_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # ==== departmet =====
        att_id_label=Label(left_inside_frame,text="Attendance Id",font=("times new roman",12,"bold"),bg="white")
        att_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        emp_id_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        emp_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # ==== attendance id =====
        att_id_label=Label(left_inside_frame,text="Attendance Id",font=("times new roman",12,"bold"),bg="white")
        att_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        emp_id_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        emp_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # ==== attendance id =====
        att_id_label=Label(left_inside_frame,text="Attendance Id",font=("times new roman",12,"bold"),bg="white")
        att_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        emp_id_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        emp_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # ==== attendance id =====
        att_id_label=Label(left_inside_frame,text="Attendance Id",font=("times new roman",12,"bold"),bg="white")
        att_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        emp_id_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        emp_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=10,width=670,height=580)




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()