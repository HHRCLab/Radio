import random
import socket
from datetime import datetime
import threading
from flask import Flask, render_template, url_for, jsonify

# Udp related stuff
# variables
IP = "0.0.0.0"
MulticastIP = '239.0.0.1'
PORT = 5050
socketlist = []
bufferSize = 4096
rf = [1, 1]
massage = "a9"
TimeOut = 5


# class Arduino:5050
#     def __init__(self, ip, port):
#         self.IP = ip
#         self.RCVPORT = port
#         self.status = False

#         self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         self.udp.bind((IP, self.RCVPORT))
#         self.udp.settimeout(TimeOut)
#         self.udp.sendto(massage.encode(encoding="utf=8"), (self.IP, PORT))
        
#         self.tempudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
         
#     def changeStatus(self, state):
#         self.status = state
#         print(f"{self.IP}:{self.status}")


#     def sendmsg(self):
#         self.tempudp.sendto(massage.encode(encoding="utf=8"), (self.IP, PORT))
#         print("resent")

#     def sendfq(self,msg,fqlength):
#         msgtosend = "Fq:" + str(fqlength) +str(msg)
#         self.tempudp.sendto(msgtosend.encode(encoding="utf=8"), (self.IP, PORT))
    
#     def reset(self):
#         msg = "RST"
#         self.tempudp.sendto(msg.encode(encoding="utf=8"), (self.IP, PORT))

# init
# socketlist.append(Arduino("192.168.10.23", 50001))
# socketlist.append(Arduino("192.168.10.27", 50002))


# def openlogs():
#     logs = open("logs.txt", "rt")
#     return logs.read()


# def tostr():
#     for x in socketlist:
#         print(x.IP, x.RCVPORT)

# def logto(id):
#     logs = open("logs.txt", "a")
#     now = datetime.now().strftime("%m.%d.%Y, %H:%M:%S")
#     logs.write(f"{now} | {id.IP}:{id.RCVPORT} is not responding\r")
#     logs.close()



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific interface and port
sock.bind((IP, 5050))

# Set socket options to join the multicast group
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MulticastIP) + socket.inet_aton('0.0.0.0'))

# Receive and process multicast packets

def main1(level):
    global rf
    while True:
        try:   
            print("in")         
            data, addr = sock.recvfrom(bufferSize)
            print("out")
            print(f"{addr}|    |{data.decode('utf-8')}")


        except socket.timeout:
            print(f"{sock.IP,sock.RCVPORT} timed out")
            continue
            


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


    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    threading.Thread(target=lambda: main1(level=rf)).start()
    # threading.Thread(target=web).start()
