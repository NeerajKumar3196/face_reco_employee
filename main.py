from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x695+0+0")
        self.root.title("Employee's Attendance Face Recognition System")


        # bg_image 

        img=Image.open(r"D:\face_rekog_attendance\face-reko-attendance\images\bg4.jpg")
        img=img.resize((1500,695),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1500,height=695)


        #title

        title_lbl =Label(bg_img,text="Employee's Face Recognition Attendance System Software",font=("times new Roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1450,height=55)


        
        #employee button

        img1=Image.open(r"D:\face_rekog_attendance\face-reko-attendance\images\employee_detail.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(bg_img,image=self.photoimg1,cursor="hand2")
        b1.place(x=100,y=150,width=150,height=150)

        b1_1=Button(bg_img,text="Employee's Details",cursor="hand2",font=("times new Roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=90,y=300,width=170,height=30)

        #face detection

        img2=Image.open(r"D:\face_rekog_attendance\face-reko-attendance\images\face_reko.png")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(bg_img,image=self.photoimg2,cursor="hand2")
        b2.place(x=400,y=150,width=150,height=150)

        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new Roman",15,"bold"),bg="blue",fg="white")
        b2_1.place(x=390,y=300,width=170,height=30)

        # attendance 

        img3=Image.open(r"D:\face_rekog_attendance\face-reko-attendance\images\face_reko.png")
        img3=img3.resize((100,100),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(bg_img,image=self.photoimg3,cursor="hand2")
        b3.place(x=100,y=400,width=150,height=150)

        b3_1=Button(bg_img,text="attendance",cursor="hand2",font=("times new Roman",15,"bold"),bg="blue",fg="white")
        b3_1.place(x=90,y=550,width=170,height=30)


        #help desk

        img4=Image.open(r"D:\face_rekog_attendance\face-reko-attendance\images\face_reko.png")
        img4=img4.resize((100,100),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b4.place(x=400,y=400,width=150,height=150)

        b4_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new Roman",15,"bold"),bg="blue",fg="white")
        b4_1.place(x=390,y=550,width=170,height=30)


        #Photos

        img5=Image.open(r"D:\face_rekog_attendance\face-reko-attendance\images\face_reko.png")
        img5=img5.resize((100,100),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b5=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b5.place(x=700,y=150,width=150,height=150)

        b5_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new Roman",15,"bold"),bg="blue",fg="white")
        b5_1.place(x=690,y=300,width=170,height=30)


        #exit

        img6=Image.open(r"D:\face_rekog_attendance\face-reko-attendance\images\face_reko.png")
        img6=img6.resize((100,100),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b6=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b6.place(x=700,y=400,width=150,height=150)

        b6_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new Roman",15,"bold"),bg="blue",fg="white")
        b6_1.place(x=690,y=550,width=170,height=30)







if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
