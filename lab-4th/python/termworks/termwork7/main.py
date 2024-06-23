from tkinter import *
# from tkinter import messagebox

class MyCalc:
    def __init__(self,root):
        try:
            self.lbl1 = Label(root,text="Enter 1st num: ",fg="blue",bg = "yellow",font = (16))
            self.lbl1.place(x=20,y=50)
           
            self.lbl1 = Label(root,text="Enter 2nd num: ",fg="blue",bg = "yellow",font = (16))
            self.lbl1.place(x=20,y=100)
           
            self.lbl1 = Label(root,text="Result is: ",fg="blue",bg = "yellow",font = (16))
            self.lbl1.place(x=20,y=150)
           
            self.tbox1 = Entry(root,font=("arial",12,"bold"),bg="white")
            self.tbox1.place(x=150,y=50)
           
            self.tbox2 = Entry(root,font=("arial",12,"bold"),bg="white")
            self.tbox2.place(x=150,y=100)
           
            self.tbox3 = Entry(root,font=("arial",12,"bold"),bg="white")
            self.tbox3.place(x=150,y=150)
            self.tbox3.config(state= "disabled")
           
            self.btnAdd = Button(root,text="Sum",command = self.Add,font=("arial",12,"bold"),bg="light blue")
            self.btnAdd.place(x=50,y=200)
           
            self.btnSub = Button(root,text="Sub",command = self.Diff,font=("arial",12,"bold"),bg="cyan")
            self.btnSub.place(x=120,y=200)
           
            self.btnMult = Button(root,text="Prod",command = self.Prod,font=("arial",12,"bold"),bg="magenta")
            self.btnMult.place(x=190,y=200)
           
            self.btnDiv = Button(root,text="Div",command = self.Div,font=("arial",12,"bold"),bg="light grey")
            self.btnDiv.place(x=260,y=200)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def validate_input(self):
        num1 = self.tbox1.get()
        num2 = self.tbox2.get()
        
        if not num1 or not num2:
            return False
        
        return True
       
    def Add(self):
        if not self.validate_input():
            self.show_error("Please enter valid numbers in both fields.")
            return
        
        self.tbox3.delete(0,END)
        self.tbox3.config(state= "normal")
        num1= int(self.tbox1.get())
        num2= int(self.tbox2.get())
        self.tbox3.insert(END, str(num1+num2))
       
    def Diff(self):
        if not self.validate_input():
            self.show_error("Please enter valid numbers in both fields.")
            return
        self.tbox3.delete(0,END)
        self.tbox3.config(state= "normal")
        num1= int(self.tbox1.get())
        num2= int(self.tbox2.get())
        self.tbox3.insert(END, str(num1-num2))
       
    def Prod(self):
        if not self.validate_input():
            self.show_error("Please enter valid numbers in both fields.")
            return
        self.tbox3.delete(0,END)
        self.tbox3.config(state= "normal")
        num1= int(self.tbox1.get())
        num2= int(self.tbox2.get())
        self.tbox3.insert(END, str(num1*num2))
       
    def Div(self):
        if not self.validate_input():
            self.show_error("Please enter valid numbers in both fields. ")
            return
        self.tbox3.delete(0,END)
        self.tbox3.config(state= "normal")
        num1= int(self.tbox1.get())
        num2= int(self.tbox2.get())
        self.tbox3.insert(END, str(num1/num2))

    def show_error(self, message):
        messagebox.showerror("Error", message)
   
root = Tk()
root.title("Calculator")
root.geometry("400x400")
root.config(bg="white")
myCalc = MyCalc(root)
root.mainloop()
