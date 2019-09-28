import socket


host, port = '127.0.0.1', 8000

s = socket.socket()
s.connect((host, port))

print("Aperte q e de enter para sair\n")
message = input("$ ")

while message != 'q':
    s.send(message.encode())
    data = s.recv(1024).decode()

    print('MAX: ' + data)
    message = input("$ ")

s.close()