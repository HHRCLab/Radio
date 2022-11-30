import builtins
import socket
import time
import tkinter as tk
import threading


class Box:
    win = tk.Tk()

    def __init__(self):
        self.x = x
        self.y = y

    def place(self, x, y):
        tk.Label(master=self.win, relief="sunken", bg="#ffffbf").grid(row=x, column=y, sticky="wens", columnspan=3, rowspan=5, pady=1, padx=1)
        tk.Label(master=self.win, text="Name", bg="grey").grid(row=x, column=y, sticky="we", columnspan=3, padx=50,
                                                               pady=3)
        tk.Label(master=self.win, text="Light", bg="grey").grid(row=x + 1, column=y, sticky="we", padx=3, pady=1)
        tk.Label(master=self.win, text=f"{5}", bg="grey", anchor="w").grid(row=x + 1, column=y + 2, sticky="we", padx=4,
                                                                           pady=1)
        tk.Label(master=self.win, text="AudioBox", bg="grey").grid(row=x + 2, column=y + 2, sticky="we", padx=4, pady=1)
        tk.Button(master=self.win, text="FqSet", bg="grey", command=lambda: print(fq.get())).grid(row=x + 3, column=y + 1,
                                                                                           sticky="we", padx=1, pady=1)
        fq = tk.Entry(master=self.win, text="FqSetTextBox", bg="grey80")
        fq.grid(row=x + 3, column=y + 2, sticky="we", padx=1, pady=1)

        tk.Button(master=self.win, text="Other", bg="grey", command=lambda: print(5)).grid(row=x + 4, column=y + 1,
                                                                                           sticky="we", padx=1, pady=1)
        tk.Label(master=self.win, text="Stats", bg="grey").grid(row=x + 4, column=y + 2, sticky="we", padx=4, pady=4)

    def init(self):
        Box.win.mainloop()

    def setSize(self):
        Box.win.grid_columnconfigure(0, minsize=20)
        Box.win.grid_columnconfigure(1, minsize=20)
        Box.win.grid_columnconfigure(2, minsize=20)
        ColumnMinSize = 15
        Box.win.grid_rowconfigure(0, minsize=ColumnMinSize)
        Box.win.grid_rowconfigure(1, minsize=ColumnMinSize)
        Box.win.grid_rowconfigure(2, minsize=ColumnMinSize)
        Box.win.grid_rowconfigure(3, minsize=ColumnMinSize)
        Box.win.grid_rowconfigure(4, minsize=ColumnMinSize)


boxforBox = []
# for s in range(15):
#     boxforBox.append(Box())
# for Box in range(15):
#     boxforBox.append(Box)

while True:

    for y in (0, 5, 10):
        for x in (0, 3, 6, 9, 12):
            # a = Box()
            # a.place(y, x)
            # boxforBox.append(a)
            # a.init()
            Box().place(y, x)


    Box.setSize(self=Box)
    Box.init(self=Box)

# window = tk.Tk()
# window.title("Title")
# window.geometry(f"700x500+350+75")
#
# Name = tk.Label(master=window, text="Name", bg="grey")
# IndicationLight = tk.Label(master=window, text="IndicationLight", bg="grey")
# LevelBox = tk.Label(master=window, text=f"{6}", bg="grey", anchor="w", width=100)
# AudioBox = tk.Label(master=window, text="AudioBox", bg="grey")
# FqSetButton = tk.Button(master=window, text="FqSetButton", bg="grey", command=lambda: print(5))
# FqSetTextBox = tk.Entry(master=window, text="FqSetTextBox", bg="grey80")
# OtherButton = tk.Button(master=window, text="OtherButton", bg="grey", command=lambda: LevelBox.grid(row=1, column=2, sticky="we"))
# Stats = tk.Label(master=window, text="Stats", bg="grey")
#
#
# Name.grid(row=0, column=0, sticky="we", columnspan=3)
# IndicationLight.grid(row=1, column=0, sticky="we")
#
# LevelBox.grid(row=1, column=2, sticky="we")
# AudioBox.grid(row=2, column=2, sticky="we")
# FqSetButton.grid(row=3, column=1, sticky="we")
# FqSetTextBox.grid(row=3, column=2, sticky="we")
# OtherButton.grid(row=4, column=1, sticky="we")
# Stats.grid(row=4, column=2, sticky="we")
#
# window.grid_columnconfigure(0, minsize=50)
# window.grid_columnconfigure(1, minsize=100)
# window.grid_columnconfigure(2, minsize=400)
# ColumnMinSize = 30
# window.grid_rowconfigure(0, minsize=ColumnMinSize)
# window.grid_rowconfigure(1, minsize=ColumnMinSize)
# window.grid_rowconfigure(2, minsize=ColumnMinSize)
# window.grid_rowconfigure(3, minsize=ColumnMinSize)
# window.grid_rowconfigure(4, minsize=ColumnMinSize)
#
# window.mainloop()
