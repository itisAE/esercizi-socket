import socket

def start_server():
    server_address = ("localhost", 22222)
    buffer_size = 4096

    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server_socket.bind(server_address)

    clients = []

    print("Server UDP in ascolto...")

    while True:
        data, address = udp_server_socket.recvfrom(buffer_size)
        if address not in clients:
            clients.append(address)
        print(f"Messaggio ricevuto da {address}: {data.decode()}")
        
        for client in clients:
            if client != address:
                udp_server_socket.sendto(data, client)
                print(f"Ho inviato un messaggio a {client}")

if __name__ == "__main__":
    start_server()
