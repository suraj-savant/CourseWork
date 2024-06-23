from tkinter import *
from tkinter import messagebox

def calculate(operation:str) :
    num1, num2 = tbox1.get(), tbox2.get()
    if not num1 or not num2 :
        messagebox.showerror("Error", message="Please Enter num1 and num2")
        return
        
    num1 = int(num1)
    num2 = int(num2)
    answer = 0

    if operation == "add" :
        answer = num1+num2
    elif operation == "sub" :
        answer = num1-num2
    elif operation == "mul" :
        answer = num1*num2
    elif operation == "div" :
        answer = num1/num2
    
    tbox3.config(state="normal")
    tbox3.delete(0,END)
    tbox3.insert(END, str(answer))
    tbox3.config(state="disabled")
    pass



if __name__ == '__main__' :
    root = Tk()
    root.title("Calculator")
    root.geometry("300x250")
    Label(root, text="Enter first number :", foreground="blue").place(x=20,y=20)
    Label(root, text="Enter second number :", foreground="blue").place(x=20,y=60)
    Label(root, text="Result :", foreground="blue").place(x=20,y=100)

    tbox1 = Entry(root,background="white")
    tbox1.place(x=160, y=20)
    tbox2 = Entry(root,background="white")
    tbox2.place(x=160, y=60)
    tbox3 = Entry(root,background="white")
    tbox3.place(x=160, y=100)
    tbox3.config(state = "disabled")

    Button(text="Sum", background="blue", foreground="white", command=lambda:calculate("add")).place(x=20, y=140)
    Button(text="Sub", background="blue", foreground="white", command=lambda:calculate("sub")).place(x=80, y=140)
    Button(text="Multiply", background="blue", foreground="white", command=lambda:calculate("mul")).place(x=140, y=140)
    Button(text="Divide", background="blue", foreground="white", command=lambda:calculate("div")).place(x=220, y=140)

    root.mainloop()