import socket
import json
import time
import datetime
import urllib.request

API="nnvBpHyP6BUcWPiePvvGcPdtTkUOhrz8"
host = '127.0.0.1'
port = 8000

nome1= "Gustavo Rodrigues"
nome2= "Igor Capeletti"

s = socket.socket()
s.bind((host, port))
s.listen(5)
print("ouvindo na porta " + str(port) + "...")

c, addr = s.accept()  # estabelece conexao com cliente
print("Conectado com ", addr)

class DeuProblema(Exception): pass

def devs():
    """
    Funcao que retorna os nomes dos desenvolvedores
    :return answer: uma string com os nomes
    """
    answer = "Developers: " + nome1 + " e " + nome2
    return answer

def dataHora():
    """
    funcao que solicita o horairo local da maquina
    :return answer: uma string com o horario atual
    """

    time = datetime.datetime.now()
    answer = "Data e hora atual: " + str(time)
    return answer

def help(argument):
    """
    funcao que retorna a lista de comandos disponiveis

    :param argument: string que representa o comando para mais informacoes
    :return: string com os comandos disponiveis ou mais informacoes sobre um comando
    """
    answer = "Os comandos devem iniciar com \  exit, devs, datahora, weather <cidade>, watherweek <cidade>, help <comando>"
    print("")
    if argument != "":
        if argument == "DEVS":
            answer = "O comando \dev contem mais informacoes sobre os desenvolvedores do MAX"
        elif argument == "DATAHORA":
            answer = "O comando \datahora retorna a data e hora atual."
        elif argument == "WEATHER":
            answer = "O comando \weather espera uma cidade como parametro, e retorna a temperatura atual desta localizacao."
        elif argument == "WEATHERWEEK":
            answer = "O comando \weatherweek espera uma cidade como parametro, e retorna a previsao do tempo num periodo de 5 dias"
        elif argument == "HELP":
            answer = "LOOOOOOOPP"
        else:
            answer = "Desculpe, nao reconheco o comando " + argument

    return answer

def weather(argument):
    """
    funcao que recebe como parametro o comando e testa se possui os parametros corretos
    caso tenha parametro certo, requisita ao servico de metereologia, via http (POST e GET) e retorna a temperatura
    atual da cidade requisitada

    :param argument: string que eh a cidade a ser pesquisada
    :return: condicao climatica atual da localizacao ou uma mensagem de erro caso a cidade nao tenha sido informada
    """
    if argument != "":
        #TODO arrumar a url
        searchAddress = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=" + API + "&q=" + argument + "&language=pt-br"
        #TODO verificar o request da urlopen
        with urllib.request.urlopen(searchAddress) as searchAddress:
            data = json.loads(searchAddress.read().decode())
            print(data)
        locationKey = data[0]['Key'] # pega o valor do campo key

        forecast = "http://dataservice.accuweather.com/locations/v1/hourly/1hour" + locationKey + "?apikey=" + API + "&language=pt-BR&details=true"
        with urllib.request.urlopen(forecast) as forecast:
            data = json.loads(forecast.read().decode())
            Fahrenheit  = data["Temperature"]["Value"]
            Celsius = (Fahrenheit - 32)/1.8000
            answer = "Temperatura em " + argument + ":" + str(Celsius) + "graus Celsius" # string que sera retornada para o cliente

    else:
        answer = "Comando necessita de uma localizacao. Digite \help para saber mais"

    return answer

#TODO
def weatherWeek(argument):
    """
    funcao que recebe uma cidade como parametro e retorna a previsao do tempo para ela, no periodo de uma semana
    :param argument: string que representa a cidade a ser pesquisada
    :return: temperatura da semana
    """
    pass


# laco principal do servidor
while True:
    data = c.recv(1024).decode()

    print("Cliente disse " + str(data))

    if not data:
        break

    isCommand = ord(data[0])  # pega o codigo ascii do primeiro character da string
    answer = data
    if isCommand == 92: # entao eh um comando
        data = data[1:] # edita a string do segundo caracter ao ultimo - retira o \
        data = data.upper() # transforma tudo em caixa alta
        command, argument = "", ""
        print("data: ", data)
        try:
            command, argument = data.split(" ")  # divide a string em espacos
        except ValueError:
            print("sem argumentos passados")
            command = data
            if command == "HELP":
                answer = help(argument)
            elif command == "DATAHORA":
                answer = dataHora()
            elif command == "DEVS":
                answer = devs()
            else:
                answer = "Comando invalido. Digite \help para saber mais"
        else:
            print("comando: " + command + " argumento: " + argument)
            if command == "HELP":
                answer = help(argument)

            elif command == "WEATHER":
                answer = weather(argument)

            elif command == "WEATHERWEEK":
                answer = weatherWeek(argument)

            else:
                answer = "Comando invalido. Digite \help para saber mais"
        finally:
            c.send(answer.encode()) # envia a resposta para o cliente
    else:
        c.send(answer.encode())



c.close()