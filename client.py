import socket

host = '127.0.0.1'
port = 8000

s = socket.socket()
s.connect((host, port))

message = input("digite q para sair $ ")

while message != 'q':
    s.send(message.encode())
    data = s.recv(1024).decode()

    print('Server diz: ' + data)

    message = input("$ ")

s.close()