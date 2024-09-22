import socket

server_address = ("192.168.1.97", 22222)  # Use localhost for testing
BUFFER_SIZE = 4092
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
NUM_INVII = 10

try:
    for i in range(NUM_INVII):
        udp_client_socket.sendto(str(i + 1).encode(), server_address)
        print("INVIO...")
except OSError as e:
    print(f"ERRORE: {e}")

udp_client_socket.close()
