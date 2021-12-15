import tkinter as tk
from menu import Menu
from buzzer_p1 import Buzzer_p1
from buzzer_p2 import Buzzer_p2
from boom import Boom


class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = {}
        self.geometry("635x260")
        self.minsize(635, 260)
        self.maxsize(635, 260)

        for F in (Menu, Buzzer_p1, Buzzer_p2, Boom):
            frame = F(self)
            self.frame[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.configure(bg="black")

        self.show_frame(Buzzer_p2)

    def show_frame(self, cont):
        frame = self.frame[cont]
        frame.tkraise()


window = Window()
window.mainloop()
