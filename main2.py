import random
import socket
import time
import threading
from flask import Flask, render_template, url_for, jsonify

IP = "192.168.1.10"
PORT = 5050
bufferSize = 8
rf = [1, 1]
rf2 = {"192.168.1.20" : 0, "192.168.1.21" : 0}
massage = "a9"
TimeOut = 7


def openlogs():
    logs = open("logs.txt", "rt")
    return logs.read()

def logto(id):
    logs = open("logs.txt", "a")
    logs.write(f"{time.ctime(1672215379.5045543)}:{id.IP}:{id.RCVPORT} is not responding\r")
    logs.close()




udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((IP,50000))


pcsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
pcsocket.bind((IP,PORT))






def main1(level):
    global rf
    while True:
        try:            
            data, addr = udp.recvfrom(bufferSize)
            rf2[addr[0]] = round(sum(list(data)[:6]) / len(list(data)[:6]))
            # sock.changeStatus(True)
            

            # print(f"Received data:{rf2[addr[0]]} from {addr}\n")
            # tostr()
            
        except socket.timeout:
            print(f"{addr} timed out")

            # sock.changeStatus(False)
            # logto(sock)
            # sock.sendmsg()
            continue


def web():

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('Home.html', rf=rf2, rflen=len(rf2))

    @app.route("/logs")
    def logs():
        return render_template("Logs.html", logs=openlogs())
    
    @app.route("/get_rf", methods=["GET"])
    def get_rf():
        return jsonify(rf2)

    # @app.route("/get_status", methods=["GET"]) 
    # def get_status():
    #     return jsonify([x.status for x in socketlist])


    app.run()


if __name__ == "__main__":
    threading.Thread(target=lambda: main1(level=rf)).start()
    # threading.Thread(target=web).start()
