# #client

import socket

server_address = ("192.168.0.1",22222) #indirizzo ip e porta in una tupla
BUFFER_SIZE = 4092  #numero di byte massimo che posso mandare e/o ricevere
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #DGRAM significa che è udp
NUM_INVII=10

try:
    for i in range(NUM_INVII):
        udp_client_socket.sendto((i+1).encode(), server_address)

except OSError as e:
    print(f"ERRORE: {e}")

udp_client_socket.close()


