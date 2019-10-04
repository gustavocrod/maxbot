import socket
import os
from util import printHelpClient, printMax, makeArgs


def clientHandler(server):
    """
    Funcao manipuladora, onde acontece toda a logica do cliente
    :param server: objeto socket responsavel pela conexao com o
    :return: pass
    """
    while True:
        printMax()
        printHelpClient()
        message = input("$ ")  # recebe o que cliente digitar

        while message != 'q':
            server.send(message.encode())  # envia para servidor o que cliente solicitou
            data = server.recv(4096).decode()  # recebe resposta do servidor
            printMax()
            print(data)  # mostra na tela resposta do servidor
            print("-------------------------")
            message = input("$ ")
            os.system("clear")
            print("[PROCESSANDO ...]")
        break

def makeConnection(host, port):
    """
    funcao responsavel por estabelecer a conexao com o servidor

    :param host: ip do host do max
    :param port: porta na qual o host esta sendo executado
    :return: pass
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, port))  # conecta com servidor TCP
    data = server.recv(4096).decode()  # recebe resposta de conexão do servidor

    if str(data) == "ACK":
        print("[INFO] Conectado ao servidor " + host + ", porta: " + str(port) + ", " + data + " recebido!")

        clientHandler(server)
        server.close()

        print("\n[INFO] Conexão encerrada com servidor!")

    else:
        print("[ERROR] A conexao com o server " + host + ", porta: " + str(port) + " Nao pode ser estabelecida\n")
        server.close()

def main():
    """
    funcao main, responsavel por criar conexao com o server do max
    :return:
    """
    args = makeArgs()

    if (args.host) and (args.port):
        makeConnection(args.host, args.port)


if __name__ == "__main__":
    main()
