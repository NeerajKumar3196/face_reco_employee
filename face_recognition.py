from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from cv2 import COLOR_BGR2GRAY
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x695+0+0")
        self.root.title("Face recog")

        # bg_image 

        img=Image.open(r"D:\face_rekog_employee\face_reco_employee\images\face1.png")
        img=img.resize((1500,695),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1500,height=695)


        b1=Button(bg_img,text="Face Recognition",command=self.face_recog,width=15,font=("times new roman",20,"bold"),bg="Dark Green",fg="White")
        b1.place(x=200,y=580,width=300,height=50)


        #title

        title_lbl =Label(bg_img,text="Face_Recognition",font=("times new Roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1450,height=55)


    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Employee_name from employee where Employee_Id="+str(id))
                e=my_cursor.fetchone()
                e="+".join(e)

                my_cursor.execute("select Job_Title from employee where Employee_Id="+str(id))
                t=my_cursor.fetchone()
                t="+".join(t)

                my_cursor.execute("select Phone_Number from employee where Employee_Id="+str(id))
                p=my_cursor.fetchone()
                p="+".join(p)

                


                if confidence>77:
                    cv2.putText(img,f"Employee_name:{e}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Job_Title:{t}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Phone_Number:{p}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]  
            return coord

        def recognize(img,clf, faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img


        faceCascade=cv2.CascadeClassifier("D:/face_rekog_employee/face_reco_employee/haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("D:/face_rekog_employee/classifier.xml")

        video_cap=cv2.VideoCapture(0)


        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()     
