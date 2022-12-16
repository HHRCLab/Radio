import builtins
import random
import socket
import time
import tkinter as tk
import threading
import UI

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
udp.sendto(massage.encode(encoding="utf=8"), (ArduinoIP, PORT))
time.sleep(1)


# Testing area
# numberOfArduinos = 5
# adrs = ["192.168.1.65", "192.168.1.66", "192.168.1.67"]
# level = ["36", "37", "38"]
# Alevel = [10, 9, 7]
#
# ard1, ard2, ard3 = [Arduino(adrs[i], level[i], Alevel[i]) for i in range(0, 3)]


def GUI():
    ui = UI.App()
    ui.UpdateLevel(random.randint(1, 34))
    ui.mainloop()



def main1():
    while True:
        global rf
        print("Im in")

        data, addr = udp.recvfrom(bufferSize)
        print(f"Received data:{list(data)} from {addr}\n")
        return list(data)
        rf = str(list(data))

        time.sleep(0.2)


if __name__ == "__main__":

    threading.Thread(target=main1).start()
    threading.Thread(target=GUI).start()
