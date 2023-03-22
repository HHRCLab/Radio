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
# status = [x.status for x in socketlist] 
TimeOut = 7


class Arduino:
    def __init__(self, ip, port):
        self.IP = ip
        self.RCVPORT = port
        self.status = False
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp.bind((IP, self.RCVPORT))
        self.udp.settimeout(TimeOut)
        self.udp.sendto(massage.encode(encoding="utf=8"), (self.IP, PORT))
        

    def changeStatus(self, state):
        self.status = state
        print(f"{self.IP}:{self.status}")


    def sendmsg(self):
        socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(massage.encode(encoding="utf=8"), (self.IP, PORT))
        print("resent")




for i in range(0, 2):
    socketlist.append(Arduino(f"192.168.1.6{5+i}", PORT+1+i))


def openlogs():
    logs = open("logs.txt", "rt")
    return logs.read()

def status():
    return str([x.status for x in socketlist])



def main1(level):
    global rf
    while True:
        for sock in socketlist:
            if sock.udp:
                # count = sock.udp.getsockname()[1] % 5051
                count = socketlist.index(sock)
                try:
                    print("in")
                    data, addr = sock.udp.recvfrom(bufferSize)
                    temp = list(data)[:6]
                    rf[count] = round(sum(temp) / len(temp))
                    print(f"Received data:{rf[count]} from {addr}\n")
                    

                except socket.timeout:
                    print(f"{sock.udp.getsockname()} timed out")
                    sock.changeStatus(False)
                    logs = open("logs.txt", "a")
                    logs.write(f"{time.ctime(1672215379.5045543)}:{sock.udp.getsockname()} is not responding\r")
                    logs.close()
                    sock.sendmsg()
                    continue

            else:
                print("f")


def web():

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('Home.html', rf=rf, rflen=len(rf), status=status)

    @app.route("/logs")
    def logs():
        return render_template("Logs.html", logs=openlogs())
    
    @app.route("/get_rf", methods=["GET"])
    def get_rf():
        return str(rf)

    @app.route("/get_status", methods=["GET"])
    def get_status():
        return str(status)

    app.run()


if __name__ == "__main__":
    threading.Thread(target=web).start()
    threading.Thread(target=lambda: main1(level=rf)).start()



