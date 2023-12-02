import threading
import time
from queue import Queue
import socket


def thread_chat(conn, addr, dest):
    print(f"Thread addr : {addr}")
    setconnect(dest)
    while True:
        data = conn.recv(1024)
        if not data:
            break

        # Faites quelque chose avec les données reçues
        print(f"Données reçues: {data.decode('utf-8')}")
        dest.send(data)
    conn.close()
    print(f"Handler for {addr} finish")


def setconnect(addr):
    # Creation Socket de connection
    socket_ = socket.create_connection(addr)
    return socket_
