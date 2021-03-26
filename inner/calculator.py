import tkinter


class Calculator:
    def __init__(self):
        self.root = tkinter.Tk()

    def set_window(self):
        self.root.title("Calculator")
        self.root.geometry("700x500")

    def mainloop(self):
        self.root.mainloop()