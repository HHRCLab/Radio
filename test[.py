import builtins
import random
import socket
import time
import tkinter as tk
import threading


class Window:
    win = tk.Tk()

    def __init__(self):
        ColumnMinSize = 15
        self.win.grid_columnconfigure(0, minsize=20)
        self.win.grid_columnconfigure(1, minsize=20)
        self.win.grid_columnconfigure(2, minsize=20)
        self.win.grid_rowconfigure(0, minsize=ColumnMinSize)
        self.win.grid_rowconfigure(1, minsize=ColumnMinSize)
        self.win.grid_rowconfigure(2, minsize=ColumnMinSize)
        self.win.grid_rowconfigure(3, minsize=ColumnMinSize)
        self.win.grid_rowconfigure(4, minsize=ColumnMinSize)


class Box:

    def __init__(self, X, Y):
        self.x = X
        self.y = Y
        self.num = 0



    def setnum(self, n):
        self.num = n

    lb1 = tk.Label()

    def place(self):
        tk.Label(master=Window.win, relief="sunken", bg="#ffffbf").grid(row=self.x, column=self.y, sticky="wens",
                                                                        columnspan=3, rowspan=5, pady=1, padx=1)
        tk.Label(master=Window.win, text=f"Name{self.num}", bg="grey").grid(row=self.x, column=self.y, sticky="we",
                                                                            columnspan=3,
                                                                            padx=50, pady=3)
        tk.Label(master=Window.win, text="Light", bg="grey").grid(row=self.x + 1, column=self.y, sticky="we", padx=3,
                                                                  pady=1)

        Box.lb1 = tk.Label(master=Window.win, text=f"{5}", bg="grey", anchor="w")
        Box.lb1.grid(row=self.x + 1, column=self.y + 2, sticky="we", padx=4, pady=1)

        tk.Label(master=Window.win, text="AudioBox", bg="grey").grid(row=self.x + 2, column=self.y + 2, sticky="we",
                                                                     padx=4, pady=1)
        tk.Button(master=Window.win, text="FqSet", bg="grey", command=lambda: print(fq.get())).grid(row=self.x + 3,
                                                                                                    column=self.y + 1,
                                                                                                    sticky="we", padx=1,
                                                                                                    pady=1)
        fq = tk.Entry(master=Window.win, text="FqSetTextBox", bg="grey80")
        fq.grid(row=self.x + 3, column=self.y + 2, sticky="we", padx=1, pady=1)

        tk.Button(master=Window.win, text="Other", bg="grey", command=lambda: print(5)).grid(row=self.x + 4,
                                                                                             column=self.y + 1,
                                                                                             sticky="we", padx=1,
                                                                                             pady=1)
        tk.Label(master=Window.win, text="Stats", bg="grey").grid(row=self.x + 4, column=self.y + 2, sticky="we",
                                                                  padx=4, pady=4)

    def init(self):
        Window.win.mainloop()

    def update(self):

        Box.lb1.config(text=random.randint(1, 10))
        Window.win.after(2000, Box.update)
        print("updated")


boxforbox = []

while True:

    for y in (0, 5, 10):
        for x in (0, 3, 6, 9, 12):
            boxforbox.append(Box(y, x))

    for i in range(0, 15):
        boxforbox[i].setnum(random.randint(1, 99))
        boxforbox[i].place()

    for i in range(0, 15):
        # boxforbox[i].update()
        pass
    for i in range(0, 15):
        boxforbox[i].lb1.config(text="dwdwdwdwdwdwdwdw")
    for i in range(0, 15):
        boxforbox[i].init()



