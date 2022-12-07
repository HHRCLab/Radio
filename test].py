import builtins
import socket
import time
import tkinter as tk
import threading
import random


class Box:
    win = tk.Tk()

    def __init__(self):
        self.test = tk.Label(master=Box.win, text="Name", bg="grey")
        # self.Background = tk.Label(master=Box.win, relief="sunken", bg="#ffffbf")
        # self.Name = tk.Label(master=Box.win, text="Name", bg="grey")
        # self.IndicationLight = tk.Label(master=Box.win, text="Light", bg="grey")
        # self.Level = tk.Label(master=Box.win, text="5", bg="grey", anchor="w")
        # self.Audio = tk.Label(master=Box.win, text="AudioBox", bg="grey")
        # self.FqSetButton = tk.Button(master=Box.win, text="FqSet", bg="grey", command=lambda: print(self.FqTextbox.get()))
        # self.FqTextbox = tk.Entry(master=Box.win, bg="grey80")
        # self.OtherButton = tk.Button(master=Box.win, text="Other", bg="grey", command=lambda: print(5))
        # self.Stats = tk.Label(master=Box.win, text="Stats", bg="grey")

    def place(self, X, Y):
        self.test.grid(row=X, column=Y)
        # self.Background.grid(row=X, column=Y, sticky="wens", columnspan=3, rowspan=5, pady=1, padx=1)
        # self.Name.grid(row=X, column=Y, sticky="we", columnspan=3, padx=50, pady=3)
        # self.IndicationLight.grid(row=X + 1, column=Y, sticky="we", padx=3, pady=1)
        # self.Level.grid(row=X + 1, column=Y + 2, sticky="we", padx=4, pady=1)
        # self.Audio.grid(row=X + 2, column=Y + 2, sticky="we", padx=4, pady=1)
        # self.FqSetButton.grid(row=X + 3, column=Y + 1, sticky="we", padx=1, pady=1)
        # self.FqTextbox.grid(row=X + 3, column=Y + 2, sticky="we", padx=1, pady=1)
        # self.OtherButton.grid(row=X + 4, column=Y + 1, sticky="we", padx=1, pady=1)
        # self.Stats.grid(row=X + 4, column=Y + 2, sticky="we", padx=4, pady=4)

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

    def init1(self):
        Box.win.mainloop()

    def update(self):
        Box.win.after(500, Box.update)
        self.test.config(text=f"{random.randint(9, 95)}")
        print("Updated")


# boxforbox = []
# boxiter = iter(boxforbox)

# while True:
#
#     for _ in range(0, 15):
#         boxforbox.append(Box())
#
#     for y in (0, 5, 10):
#         for x in (0, 3, 6, 9, 12):
#             next(boxiter).place(y, x)
#
#     for n in boxiter:
#         n.setSize()
#
#     for n in boxiter:
#         n.update()
#
#     for n in range(0, 15):
#         boxforbox[n].init()


box1 = Box()
box1.place(0, 0)
box1.update()
box1.init1()


