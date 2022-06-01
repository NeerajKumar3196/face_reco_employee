from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x695+0+0")
        self.root.title("Employee's Attendance Face Recognition System")






if __name__ == "__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
