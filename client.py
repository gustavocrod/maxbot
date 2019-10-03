import socket
import time

host, port = 'localhost', 8000

# timeout= 0.2

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))  # conecta com servidor TCP
data = server.recv(4096).decode()  # recebe resposta de conexão do servidor

if str(data) == "ACK":
    print("Conectado ao servidor " + host + ", porta: " + str(port) + ", " + data + " recebido!")
    # time.sleep(timeout)   #timeout de espera para resposta do servidor

    while True:

        print("Aperte q e de enter para sair\n")
        message = input("$ ")  # recebe o que cliente digitar

        while message != 'q':
            server.send(message.encode())  # envia para servidor o que cliente solicitou
            data = server.recv(4096).decode()  # recebe resposta do servidor

            print('-- MAX: \n' + data)  # mostra na tela resposta do servidor
            message = input("$ ")

        break
    server.close()
    print("\nConexão encerrada com servidor!")
else:
    print("Não conseguiu conectar ao servidor " + host + ", porta: " + str(port))
    server.close()