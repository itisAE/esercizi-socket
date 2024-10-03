import socket
from pynput.keyboard import Listener, Key

host = 'localhost'
port = 22333
buffer_size = 4096



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def on_press(key):

    print('Pressed key:', key)
    value = 55

    valAcc=['w','a','s','d']
    if key.char in valAcc:
        message = f"{key},{value}"
        s.sendall(message.encode())

        data = s.recv(buffer_size)
        if data.decode() == "ok":
            print("Movement executed correctly")
        else:
            print("Movement not valid")

with Listener(on_press=on_press) as listener:
    listener.join()