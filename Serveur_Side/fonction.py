import threading


def thread_chat(conn, addr):
    print(f"Thread addr : {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        # Faites quelque chose avec les données reçues
        print(f"Données reçues: {data.decode('utf-8')}")
        # message
        message = "Message reçu"
        # Répondre au client
        conn.send(message.encode())

    addr.close()
