import tkinter as tk

class Calculator :
    def __init__(self, root:tk.TK) -> None:
        self.root =root
        pass

    def build_gui(self) :
        self.root.title="Hello  World"

    def runapp(self) :
        self.root.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    cal = Calculator(root)
    cal.runapp()
   