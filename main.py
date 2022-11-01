import builtins
import socket
import time
import tkinter as tk
import threading

global rf
rf = 1

def SetFq():
    print(FqSetTextbox.get())
    pass


class Arduino:
    def __init__(self, address, signalLevel, AudioLevel):
        self.address = address
        self.signalLevel = signalLevel
        self.AudioLevel = AudioLevel

    def getadress(self):
        return self.address

    def getsignalLevel(self):
        return self.signalLevel

    def getAudioLevel(self):
        return self.AudioLevel

    def setaddress(self, address):
        self.address = address

    def setsignalLevel(self, signalLevel):
        self.signalLevel = signalLevel

    def setAudioLevel(self, AudioLevel):
        self.AudioLevel = AudioLevel

    def __str__(self):
        return f"({self.address},{self.signalLevel},{self.AudioLevel})"

    def signalStatus(self):
        pass

    def audioStatus(self):
        pass


def udp():
    # variables
    IP = "192.168.1.10"
    ArduinoIP = "192.168.1.65"
    PORT = 5050
    bufferSize = 2048

    # Udp related stuff
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # print(socket.gethostbyname(socket.getfqdn()))

    udp.bind((IP, PORT))
    massage = "a"
    # massage2 = "Fr:" + input("Enter your desired frequency:").replace(".", "")
    udp.sendto(massage.encode(encoding="utf=8"), (ArduinoIP, PORT))
    time.sleep(1)

    # Testing area
    numberOfArduinos = 5
    adrs = ["192.168.1.65", "192.168.1.66", "192.168.1.67"]
    level = ["36", "37", "38"]
    Alevel = [10, 9, 7]

    ard1, ard2, ard3 = [Arduino(adrs[i], level[i], Alevel[i]) for i in range(0, 3)]

    # print(ard1, ard2, ard3)

    # Main function
    while True:
        global rf
        print("Im in")
        # Receive data block
        data, addr = udp.recvfrom(bufferSize)

        print(f"Received data:{list(data)} from {addr}\n")

        rf = str(list(data))

        # dt = data.decode().replace("\\x0", " ").split()
        # print(str(data).replace("\\x0", " ").replace("b" and "'", "").split())

        # Send data block
        time.sleep(0.2)
        # udp.sendto(massage2.encode(encoding="utf=8"), (ArduinoIP, PORT))


def checkData():
    pass


threading.Thread(target=udp).start()


# GUI
window = tk.Tk()
window.title("Title")
window.geometry(f"700x500+350+75")

Name = tk.Label(master=window, text="Name", bg="grey")
IndicationLight = tk.Label(master=window, text="IndicationLight", bg="grey")
LevelBox = tk.Label(master=window, text=f"{rf}", bg="grey", anchor="w", width=100)
AudioBox = tk.Label(master=window, text="AudioBox", bg="grey")
FqSetButton = tk.Button(master=window, text="FqSetButton", bg="grey", command=SetFq)
FqSetTextbox = tk.Entry(master=window, text="FqSetTextbox", bg="grey80")
OtherButton = tk.Button(master=window, text="OtherButton", bg="grey", command=lambda: LevelBox.grid(row=1, column=2, sticky="we"))
Stats = tk.Label(master=window, text="Stats", bg="grey")

window.mainloop()
Name.grid(row=0, column=0, sticky="we", columnspan=3)
IndicationLight.grid(row=1, column=0, sticky="we")

LevelBox.grid(row=1, column=2, sticky="we")
AudioBox.grid(row=2, column=2, sticky="we")
FqSetButton.grid(row=3, column=1, sticky="we")
FqSetTextbox.grid(row=3, column=2, sticky="we")
OtherButton.grid(row=4, column=1, sticky="we")
Stats.grid(row=4, column=2, sticky="we")

window.grid_columnconfigure(0, minsize=50)
window.grid_columnconfigure(1, minsize=100)
window.grid_columnconfigure(2, minsize=400)
ColumnMinSize = 30
window.grid_rowconfigure(0, minsize=ColumnMinSize)
window.grid_rowconfigure(1, minsize=ColumnMinSize)
window.grid_rowconfigure(2, minsize=ColumnMinSize)
window.grid_rowconfigure(3, minsize=ColumnMinSize)
window.grid_rowconfigure(4, minsize=ColumnMinSize)

window.mainloop()
