import socket

host = '127.0.0.1'
port = 8000

s = socket.socket()
s.bind((host, port))
s.listen(5)
print("ouvindo na porta " + str(port) + "...")

c, addr = s.accept()  # estabelece conexao com cliente
print("Conectado com ", addr)
while True:
    data = c.recv(1024).decode()
    test = "Olaaaaa sou o M.A.X"
    if not data:
        break

    print("Cliente diz " + str(data))

    print("Enviando: " + str(test))
    c.send(test.encode())

c.close()