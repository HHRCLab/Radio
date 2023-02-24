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
bufferSize = 128
rf = [1, 1]
massage = "a9"
status = {"192.168.1.66": 1, "192.168.1.65": 1}


def sendmsgagain(tup):
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(massage.encode(encoding="utf=8"), arduinolist[tup])
    print("resent")


for i in range(len(arduinolist)):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind((IP, PORT+i+1))
    udp.settimeout(7)
    socketlist.append(udp)


for i in range(len(arduinolist)):
    socketlist[i].sendto(massage.encode(encoding="utf=8"), arduinolist[i])
time.sleep(1)


def main1(level):
    global rf
    while True:
        for sock in socketlist:
            if sock:
                count = sock.getsockname()[1] % 5051
                try:
                    print("in")
                    data, addr = sock.recvfrom(bufferSize)
                    temp = list(data)[:6]
                    rf[count] = round(sum(temp) / len(temp))
                    print(f"Received data:{rf[count]} from {addr}\n")

                except socket.timeout:
                    print(f"{sock.getsockname()} timed out")
                    sendmsgagain(count)
                    continue

            else:
                print("f")


def web():

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('Home.html', rf=rf, rflen=len(rf), status=status)

    @app.route("/get_rf")
    def get_rf():
        return str(rf)

    app.run()


if __name__ == "__main__":
    threading.Thread(target=web).start()
    threading.Thread(target=lambda: main1(level=rf)).start()



