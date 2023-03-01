import random
import socket
import time
import threading
from flask import Flask, render_template, url_for

# Udp related stuff
# variables
IP = "192.168.1.10"
PORT = 5050
arduinolist = {"192.168.1.66": (PORT, PORT+1), "192.168.1.65": (PORT, PORT+2)}
socketlist = []
bufferSize = 128
rf = [1, 1]
massage = "a9"
green = 12
yellow = 6
red = 2
status = {"0": True, "1": True}



def sendmsgagain(tup):
    x = list(arduinolist.keys())
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(massage.encode(encoding="utf=8"), (x[tup], arduinolist[x[0]][0]))
    print("resent")


for i in arduinolist.values():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind((IP, i[1]))
    udp.settimeout(7)
    socketlist.append(udp)


for i in range(len(arduinolist)):
    x = list(arduinolist.keys())
    socketlist[i].sendto(massage.encode(encoding="utf=8"), (x[i], arduinolist[x[0]][0]))
time.sleep(1)

def changestatus(tup,state):
    if state:
        status.update({f"{tup}": True})
    else:
        status.update({f"{tup}": False})
    print(status)



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
                    changestatus(count, True)

                except socket.timeout:
                    print(f"{sock.getsockname()} timed out")
                    changestatus(count, False)
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



