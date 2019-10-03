import socket
import time
import os

host, port = 'localhost', 8000

# timeout= 0.2

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))  # conecta com servidor TCP
data = server.recv(4096).decode()  # recebe resposta de conexão do servidor

if str(data) == "ACK":
    print("[INFO] Conectado ao servidor " + host + ", porta: " + str(port) + ", " + data + " recebido!")
    # time.sleep(timeout)   #timeout de espera para resposta do servidor

    while True:
        print("[HELP] Digite \help para listar os comandos disponiveis do M.A.X\n")
        print("[HELP] Aperte 'q' e de enter para sair\n")
        message = input("$ ")  # recebe o que cliente digitar

        while message != 'q':
            server.send(message.encode())  # envia para servidor o que cliente solicitou
            data = server.recv(4096).decode()  # recebe resposta do servidor

            print('---------- MAX ----------\n' + data)  # mostra na tela resposta do servidor
            print("-------------------------")
            message = input("$ ")
            os.system("clear")
            print("[PROCESSANDO ...]")

        break
    server.close()
    print("\n[INFO] Conexão encerrada com servidor!")

else:
    print("[ERROR] A conexao com o server " + host + ", porta: " + str(port) + " Nao pode ser estabelecida\n")
    server.close()