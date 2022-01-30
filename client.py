import threading
import socket
import time
from base64 import b64decode as bd

from interface import *


HOST = ""
PORT = 4444

w = []


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

gui = Interface(client)
t1 = threading.Thread(target=gui.create,args=[w])
t1.start()

time.sleep(3)
gui.update("Connecting To Server...\n",w[0])
while True:
    try:
        client.connect((HOST,PORT))
        break
    except:
        continue


msg = client.recv(1028).decode("utf-8")
gui.update(msg,w[0])


def rec_msg():
    global gui
    while True:
        try:
            msg = client.recv(1028).decode("utf-8")
            gui.update(msg,w[0])
        except:
            continue


t2 = threading.Thread(target=rec_msg)
t2.start()


