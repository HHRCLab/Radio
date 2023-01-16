import builtins
import random
import socket
import time
import tkinter as tk
import threading
import UI

def SetFq():
    print(FqSetTextbox.get())
    pass


# Udp related stuff
#       variables
IP = "192.168.1.10"
ArduinoIP = "192.168.1.65"
PORT = 5050
bufferSize = 64


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp.bind((IP, PORT))
massage = "a9"
udp.sendto(massage.encode(encoding="utf=8"), (ArduinoIP, PORT))
time.sleep(1)


class gui():
    def __init__(self):
        self.ui = UI.App()

    def GUIUpdate(self, data):

        self.ui.Frame1.updateData = data


    def go(self):
        self.ui.mainloop()




rf = 1
def main1():
    global rf
    while True:
        data, addr = udp.recvfrom(bufferSize)
        print(f"Received data:{list(data)[:6]} from {addr}\n")
        rf = list(data)[:6]

def two():
    while True:
        wind.GUIUpdate(rf)



if __name__ == "__main__":

    threading.Thread(target=main1).start()
    # threading.Thread(target=wind.GUI).start()
    # wind.GUIUpdate(rf)

    wind = gui()
    # wind.GUI()
    threading.Thread(target=two).start()
    wind.go()


    # threading.Thread(target=main1).start()
    # threading.Thread(target=gui().GUI).start()
    # threading.Thread(target=gui().GUIUpdate, args=(rf,)).start()


    # rf = Udp_data()
    # # rf.main1()
    # # print(rf.rf1)
    # threading.Thread(target=rf.main1(udp), daemon=True).start()
    # threading.Thread(target=GUI, args=(4,)).start()

    # rf = Udp_data()
    # rf.main1(udp)
    # print(rf.rf1)