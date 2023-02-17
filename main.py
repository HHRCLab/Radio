import random
import socket
import time
import threading
from flask import Flask, render_template, url_for

# Udp related stuff
# variables
IP = "192.168.1.10"
PORT = 5050
arduinolist = [("192.168.1.66", PORT), ("192.168.1.65", PORT)]
socketlist = []
bufferSize = 64
rf = 1
massage = "a9"


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(len(arduinolist)):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind((IP, PORT+i+1))
    socketlist.append(udp)


for i in range(len(arduinolist)):
    socketlist[i].sendto(massage.encode(encoding="utf=8"), arduinolist[i])
    socketlist[i].sendto(massage.encode(encoding="utf=8"), arduinolist[i])
time.sleep(1)


def main1():
    global rf
    while True:
        for sock in socketlist:
            data, addr = sock.recvfrom(bufferSize)
            print(f"Received data:{list(data)[:6]} from {addr}\n")
            rf = list(data)[:6]


def web():

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('Home.html', rf=rf)

    app.run()


if __name__ == "__main__":
    threading.Thread(target=web).start()
    threading.Thread(target=main1).start()



