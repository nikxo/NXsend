import threading
import time


def thread_chat(conn, addr):
    print(f"Thread addr : {addr}")
    while True:
        # data = conn.recv(1024)
        # if not data:
        #     break

        # # Faites quelque chose avec les données reçues
        # print(f"Données reçues: {data.decode('utf-8')}")

        message = "Message reçu"
        conn.send(message.encode())
        # Attendre 10 secondes avant d'envoyer le prochain message
        time.sleep(10)

    conn.close()
    print(f"Handler for {addr} finish")
