import threading
import socket

HOST = ""
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print("Waiting for Connections")

clients = []

def broadcast_message(message, c):
    global clients
    for client in clients:
        if client[0] == c[0]:
            pass
        else:
            msg = f"\n{c[1]}: {message} \n"
            client[0].send(msg.encode("utf-8"))


def incomming_messages(client):
    try:
        while True:
            msg = client[0].recv(1028).decode("utf-8")
            print(f"{client[1]}: {msg}")
            t3 = threading.Thread(target=broadcast_message,args=[msg,client])
            t3.start()
    except:
        print(client[1] + " Has Disconnected")
        broadcast_message(f"Disconnected", client)
        clients.remove(client)
        client[0].close()


def accept_connections():
    global clients
    try:
        while True:
            client, address = server.accept()
            print(f"{address} Connected")
            client.send("Enter a nickname".encode("utf-8"))
            nickname = client.recv(1028).decode("utf-8")
            cl = [client, nickname]
            clients.append(cl)
            t2 = threading.Thread(target=incomming_messages, args=[cl])
            t2.start()
            client.send("\nConnected\n".encode("utf-8"))
            broadcast_message(f"Connected",cl)
    except:
        try:
            print(cl[1] + " Has Disconnected")
            broadcast_message(f"Disconnected", cl)
            clients.remove(cl)
            client.close()
        except:
            pass




t1 = threading.Thread(target=accept_connections)
t1.start()
