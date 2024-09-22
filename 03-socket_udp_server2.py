# #server

import socket

server_address = ("192.168.1.97",22222) #indirizzo ip e porta in una tupla
BUFFER_SIZE = 4092  #numero di byte massimo che posso mandare e/o ricevere
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #DGRAM significa che è udp
udp_server_socket.bind(server_address) 
data=""
print("Start")
while data != "10":
    data,address=udp_server_socket.recvfrom(BUFFER_SIZE) #comando bloccante, in ascolto...
    data=data.decode()
    print(data)

udp_server_socket.close()