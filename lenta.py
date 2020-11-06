from tkinter.ttk import Progressbar
from tkinter import *

class LentaGUI():
    def __init__(self, end_number, where_to_put_the_bar):
        # self.root = Tk()
        # self.top_prgs = Toplevel()
        self.holder = where_to_put_the_bar
        self.nn = end_number
        self.prgs = Progressbar(self.holder)
        self.lbl = Label(self.holder, font="arial 15 bold")

    def update_with(self, number):
        self.prgs.config(style="TProgressbar", length=400, mode="determinate", maximum=self.nn,
                         value=0)
        self.lbl.pack(side=TOP, fill=X)
        self.prgs.pack(side=TOP)
        self.lbl.config(text=str(int((((number) / self.nn) * 100)))+"%")
        self.prgs["value"] = number
        self.prgs.update_idletasks()
        self.prgs.update_idletasks()
        if number >= self.nn:
            print('done')
            self.prgs.destroy()
            self.lbl.destroy()
            # self.holder.destroy()


