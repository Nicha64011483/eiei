import tkinter as tk
import buzzer_p1

LARGE_FONT = ("Verdana", 24)


class Menu(tk.Frame):
    def __init__(self, parent):

        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="MENU")
        label1.pack(padx=1, pady=1)

        self.parent = parent
        self.photo = tk.PhotoImage(file=r"/Users/prim/PycharmProjects/python_2/photo.png")
        label = tk.Label(image=self.photo)
        label.image = self.photo
        imgLabel = tk.Label(self, image=self.photo)
        imgLabel.pack()

        btn1 = tk.Button(self, text='Buzzer', fg="black", command=lambda: parent.show_frame(buzzer_p1.Buzzer_p1))
        btn1.pack(padx=2, pady=2)




