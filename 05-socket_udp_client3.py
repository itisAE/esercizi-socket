# #client

import socket

server_address = ("192.168.1.97",22222) #indirizzo ip e porta in una tupla
BUFFER_SIZE = 4092  #numero di byte massimo che posso mandare e/o ricevere
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #DGRAM significa che è udp


while 1:
    try:
        message=input("Inserisci un messaggio da inviare: ")
        udp_client_socket.sendto(message.encode(), server_address)
        data, address =udp_client_socket.recvfrom(BUFFER_SIZE)
        print(f'Messaggio ricevuto: {data.decode()}')  #decodifica dei dati

    except OSError as e:
        print(f"ERRORE: {e}")


udp_client_socket.close()