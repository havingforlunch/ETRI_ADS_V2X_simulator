from threading import Thread
from socket import *
from PyQt5.QtCore import *
from graph_chart import *
import struct
ads_speed = car2_speed = car1_speed = 0

class ServerSocket(QObject):
    global send_msg
    update_signal = pyqtSignal(tuple, bool)
    recv_signal = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.bListen = False
        self.clients = []
        self.ip = []
        self.threads = []

        self.update_signal.connect(self.parent.updateClient)
        self.recv_signal.connect(self.parent.updateMsg)

    def __del__(self):
        self.stop()

    def start(self):
        self.server = socket(AF_INET, SOCK_DGRAM)
        self.client = socket(AF_INET, SOCK_DGRAM)

        try:
            self.server.bind(("localhost", 55555))
        except Exception as e:
            print('Bind Error : ', e)
            return False
        else:
            self.bListen = True
            self.t = Thread(target=self.receive, args=())
            self.t.start()

        return True

    def stop(self):
        self.bListen = False
        if hasattr(self, 'server'):
            self.server.close()
            print('Logging stop')

    def receive(self):
        global ads_speed, car2_speed, car1_speed
        while True:
            try:
                msg, self.addr = self.server.recvfrom(90000)

            except:
                print('Logging stop')
                break
            else:
                if msg:
                    if msg.decode()[:5] == "speed":
                        ads_speed = int(msg.decode()[5:8])
                        car1_speed = int(msg.decode()[8:11])
                        car2_speed = int(msg.decode()[11:14])
                    else:
                        self.recv_signal.emit(str(msg.decode()))

    def send(self, test_msg):
        try:
            self.server.sendto(test_msg, self.addr)

        except Exception as e:
            print('Send() Error : ', e)

    def removeClient(self, client):
        # find closed client index
        idx = -1
        for k, v in enumerate(self.clients):
            if v == client:
                idx = k
                break

        del (self.threads[idx])
        self.update_signal.emit(False)
        self.resourceInfo()

    def removeAllClients(self):
        for c in self.clients:
            c.close()

        for addr in self.ip:
            self.update_signal.emit(addr, False)

        self.ip.clear()
        self.clients.clear()
        self.threads.clear()

        self.resourceInfo()

    def resourceInfo(self):
        print('Number of Client ip\t: ', len(self.ip))
        print('Number of Client socket\t: ', len(self.clients))
        print('Number of Client thread\t: ', len(self.threads))
