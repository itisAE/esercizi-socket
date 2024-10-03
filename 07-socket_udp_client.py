import socket
import threading


#client non bloccante
def receive_messages(udp_client_socket, buffer_size):
    while True:
        try:
            data, address = udp_client_socket.recvfrom(buffer_size)
            print(f"Messaggio ricevuto: {data.decode()}")
        except:
            break

def start_client():
    server_address = ("localhost", 22222)  # Cambia con l'indirizzo IP del server
    buffer_size = 4096  #buffer per memorizzare le informazioni in input

    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #AF_INET-->IPv4  SOCK_DGRAM-->UDP

    #il flag deamon fa si che una volta morto il main muoiano in automatico anche i vari thread che ha creato il programma
    threading.Thread(target=receive_messages, args=(udp_client_socket, buffer_size),daemon=True).start()    #starta il thread


    print("Client UDP avviato. Digita i messaggi da inviare:")
    
    while True:
        message = input()
        udp_client_socket.sendto(message.encode(), server_address)

if __name__ == "__main__":
    start_client()
