import tkinter as tk
import menu
import buzzer_p2

LARGE_FONT = ("Verdana", 24)


class Buzzer_p1(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="Buzzer")
        label1.pack(padx=5, pady=5)

        label2 = tk.Label(self, text="How to play?")
        label2.pack(padx=10, pady=10)

        label3 = tk.Label(self, text="1.Click any bottons you want\n 2.The game master will randomly choose a loser\n "
                                     "3.The loser have to drink!")
        label3.pack(padx=15, pady=15)

        btn = tk.Button(self, text="Menu", fg="black", command=lambda: parent.show_frame(menu.Menu))
        btn.pack(padx=20, pady=20)

        btn2 = tk.Button(self, text="Play", fg="black", command=lambda: parent.show_frame(buzzer_p2.Buzzer_p2))
        btn2.pack()
