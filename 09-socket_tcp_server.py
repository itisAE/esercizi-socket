import socket


host = '192.168.1.97'
port = 22222
buffer_size = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
    conn, addr = s.accept()
    print(f"Connessione avvenuta da {addr}")

    while True:
        try:
            data = conn.recv(buffer_size)
            if not data:
                break
            data=data.decode()
            dati=data.split(",")
            movimento=int(dati[0])
            valore=int(dati[1])

            if movimento in range (1,5) and valore in range(100):
                message = "ok"
                print(f"{movimento},{valore}")
            else:
                message="err"
            conn.sendall(message.encode())
        except ConnectionResetError:
            print("Connessione chiusa dal client")
            break

    conn.close()