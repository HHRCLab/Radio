import random
import socket
import time
import threading
from flask import Flask, render_template, url_for, jsonify

# Udp related stuff
# variables
IP = "192.168.1.10"
PORT = 5050
# arduinolist = {"192.168.1.66": (PORT, PORT+1), "192.168.1.65": (PORT, PORT+2)}
socketlist = []
bufferSize = 8
rf = [1, 1]
massage = "a9"
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
        
        self.tempudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        
    def changeStatus(self, state):
        self.status = state
        print(f"{self.IP}:{self.status}")


    def sendmsg(self):
        self.tempudp.sendto(massage.encode(encoding="utf=8"), (self.IP, PORT))
        print("resent")



# init
# socketlist.append(Arduino("192.168.1.20", 50000))
# socketlist.append(Arduino("192.168.1.21", 50000))


def openlogs():
    logs = open("logs.txt", "rt")
    return logs.read()


def tostr():
    for x in socketlist:
        print(x.IP, x.RCVPORT)

def logto(id):
    logs = open("logs.txt", "a")
    logs.write(f"{time.ctime(1672215379.5045543)}:{id.IP}:{id.RCVPORT} is not responding\r")
    logs.close()



def main1(level):
    global rf
    while True:
        for sock in socketlist:
            if sock.udp:
                count = socketlist.index(sock)
                try:            
                    data, addr = sock.udp.recvfrom(bufferSize)
                    rf[count] = round(sum(list(data)[:6]) / len(list(data)[:6]))
                    sock.changeStatus(True)

                    print(f"Received data:{rf[count]} from {addr}\n")
                    # tostr()
                    
                except socket.timeout:
                    print(f"{sock.IP,sock.RCVPORT} timed out")

                    sock.changeStatus(False)
                    logto(sock)
                    sock.sendmsg()
                    continue

            else:
                print("f")


def web():

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('Home.html', rf=rf, rflen=len(rf))

    @app.route("/logs")
    def logs():
        return render_template("Logs.html", logs=openlogs())
    
    @app.route("/get_rf", methods=["GET"])
    def get_rf():
        return jsonify(rf)

    @app.route("/get_status", methods=["GET"]) 
    def get_status():
        return jsonify([x.status for x in socketlist])


    app.run()


if __name__ == "__main__":
    threading.Thread(target=lambda: main1(level=rf)).start()
    threading.Thread(target=web).start()
