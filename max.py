import datetime
import json
import requests
import socket
import time
import urllib.parse
import urllib.request
import threading
import os

# APIs do AccuWeather
# API = "5EHm0OouVq2MYsFa91FGKPadu6raFZEF"
API = "nnvBpHyP6BUcWPiePvvGcPdtTkUOhrz8"

# APIs do Yandex tradutor
API_T = 'trnsl.1.1.20190927T202249Z.ae7d6ae63ea79bdc.69b6616a32a45b1f3412c33ac2de768277b6515c'
urlt = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

# informacoes do nosso servidor
ip = 'localhost'
port = 8000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(0)

ack = "ACK"

print("[LOG] Escutando " + str(ip) + ":" + str(port) + "...\n")  # inicia servidor


def devs():
    """
    Funcao que retorna os nomes dos desenvolvedores
    :return answer: uma string com os nomes
    """
    answer = "[DEVS] Developers: \n1 - Gustavo Rodrigues \n2 - Igor Capeletti"
    return answer


def dataHora():
    """
    funcao que solicita o horairo local da maquina
    :return answer: uma string com o horario atual
    """
    time = datetime.datetime.now()
    answer = "[TIME] Data e hora atual: " + str(time)
    return answer


def help(argument):
    """
    funcao que retorna a lista de comandos disponiveis
    :param argument: string que representa o comando para mais informacoes
    :return: string com os comandos disponiveis ou mais informacoes sobre um comando
    """
    if argument != "":
        argument = argument.upper()
        if argument == "DEVS":
            answer = "[HELP] O comando \devS contem mais informacoes sobre os desenvolvedores do MAX"
        elif argument == "DATAHORA":
            answer = "[HELP] O comando \datahora retorna a data e hora atual."
        elif argument == "WEATHER":
            answer = "[HELP] O comando \weather espera uma cidade como parametro, e retorna a temperatura atual desta localizacao."
        elif argument == "WEATHERWEEK":
            answer = "[HELP] O comando \weatherweek espera uma cidade como parametro, e retorna a previsao do tempo num periodo de 5 dias"
        elif argument == "HELP":
            answer = "[???] LOOOOOOOPP"
        else:
            answer = "[ERROR] Desculpe, nao reconheco o comando \help" + argument
    else:
        answer = "[HELP] Comandos:\n \devs\n \datahora\n \weather <cidade>\n \weatherweek <cidade>\n \help <comando>"
        print(answer)

    return answer


def weather(argument):
    """
    funcao que recebe como parametro o comando e testa se possui os parametros corretos
    caso tenha parametro certo, requisita ao servico de metereologia, via http (POST e GET) e retorna a temperatura
    atual da cidade requisitada

    :param argument: string que eh a cidade a ser pesquisada
    :return: condicao climatica atual da localizacao ou uma mensagem de erro caso a cidade nao tenha sido informada
    """
    if argument != "":  # TODO implementar o proprio HTTP
        print("[LOG] Pesquisando previsão...")
        requisicao = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?q=' + argument + '&appid=778c214add5c6263ad53043ba7bf546d')
        tempo = json.loads(requisicao.text)
        status = tempo['weather'][0]['description']
        qChuva = 0
        if tempo['weather'][0]['main'] == "Rain" and 'rain' in tempo:
            qChuva = list(tempo['rain'].values())[0]

        print("[LOG] Traduzindo...")
        params = dict(key=API_T, text=status, lang='en-pt')
        res = requests.get(urlt, params=params)
        jsonT = res.json()
        status = str(jsonT['text'][0])
        answer = "[FORECAST] Cidade " + argument + "\nStatus atual: " + status + "\nPrevisão de " + str(
            qChuva) + "mm\nTemperatura atual: " + str(
            round((float(tempo['main']['temp'])) - 273.15)) + "°C\nUmidade em " + str(
            tempo['main']['humidity']) + "%\nVelocidade do vento em " + str(
            round((float(tempo['wind']['speed'])) * 3.6)) + " km/h"
    else:
        answer = "[ERROR] Comando \weather necessita de uma localizacao. Digite \help para saber mais"

    return answer


def weatherWeek(argument):
    """
    funcao que recebe uma cidade como parametro e retorna a previsao do tempo para ela, no periodo de uma semana
    :param argument: string que representa a cidade a ser pesquisada
    :return: temperatura da semana
    """
    if argument != "":  # TODO implementar o proprio HTTP
        print("[LOG] Cidade " + argument + " recebida do cliente!")
        city = urllib.parse.quote(str(argument))

        print("[LOG] Cidade " + str(city) + " recebida do cliente e transformada para formato URLs!")
        print("[LOG] Pesquisando previsão...")

        # search_address="http://dataservice.accuweather.com/locations/v1/cities/IN/search?apikey="+API+"&q="+city+"&details=true"
        search_address = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=" + API + "&q=" + city + "&details=true"
        with urllib.request.urlopen(search_address) as search_address:
            data = json.loads(search_address.read().decode())
            location_key = data[0]['Key']
            daily_forcastUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + location_key + "?apikey=" + API + "&details=true"

            with urllib.request.urlopen(daily_forcastUrl) as daily_forcastUrl:
                data = json.loads(daily_forcastUrl.read().decode())
                resp = ""
                print("[LOG] Traduzindo...")
                for key1 in data['DailyForecasts']:
                    tempMin = round(((key1['Temperature']['Minimum']['Value']) - 32) / 1.8000)
                    tempMax = round(((key1['Temperature']['Maximum']['Value']) - 32) / 1.8000)

                    # parte da temperatura durante o dia
                    ventoD = round((key1['Day']['Wind']['Speed']['Value']) * 1.609)
                    qChuvaD = round((key1['Day']['Rain']['Value']) * 25.4)
                    statusD = key1['Day']['LongPhrase']
                    paramsD = dict(key=API_T, text=statusD, lang='en-pt')
                    resD = requests.get(urlt, params=paramsD)
                    jsonTD = resD.json()
                    statusD = str(jsonTD['text'][0])

                    # parte da temperatura durante a noite---------------------------------------
                    ventoN = round((key1['Night']['Wind']['Speed']['Value']) * 1.609)
                    qChuvaN = round((key1['Night']['Rain']['Value']) * 25.4)
                    statusN = key1['Night']['LongPhrase']
                    paramsN = dict(key=API_T, text=statusN, lang='en-pt')
                    resN = requests.get(urlt, params=paramsN)
                    jsonTN = resD.json()
                    statusN = str(jsonTN['text'][0])

                    diaData = key1['Date']
                    resp = resp + ("\n-----------\n"
                                   "Data: " + diaData[8:10] + "/" + diaData[5:7] + "/"
                                   + diaData[0:4] + "\nTemperatura mínima: " + str(
                        tempMin) + "\nTemperatura máxima: " + str(
                        tempMax) + "\n--Durante o dia:" + "\nPrevisão do tempo: " + statusD + "\nChuva " + str(
                        qChuvaD) + "mm\nVento " + str(
                        ventoD) + "km/h\n--Durante a noite:" + "\nPrevisão do tempo: " + statusN + "\nChuva " + str(
                        qChuvaN) + "mm\nVento " + str(ventoN) + "km/h")

                answer = "[FORECAST] Previsão do tempo para " + argument + " durante os próximos dias:\n" + resp

    else:
        answer = "[ERROR] Comando \weatherweek necessita de uma localizacao. Digite \help para saber mais"

    return answer


# parte de threads do servidor
def conecta(client, endereco):
    """
        Funcao que roda em cada thread, conecta com um cliente
    :param client:
    :param endereco: vetor que contem o ip e porta do cliente
    :return:
    """
    print("[LOG] Conectado com cliente " + str(endereco[0]) + ":" + str(endereco[1]))
    client.send(str(ack).encode())  # envia ACK para o cliente(confirmação de conexão com este servidor)
    print("[LOG] ACK enviada para cliente!")

    cont = 1
    while True:
        data = client.recv(4096).decode()  # aguarda até cliente enviar alguma mensagem e salva na variável data
        print("-------- Cliente " + str(endereco[0]) + ":" + str(endereco[1]) + " ---- Solicitação " + str(
            cont) + " ----")
        cont = cont + 1

        if not data:
            print("[LOG] Cliente desconectou!")
            break

        isCommand = ord(data[0])  # pega o codigo ascii do primeiro character da string
        if isCommand == 92:  # entao eh um comando 92 == '\'
            data = data[1:]  # recebe string do segundo caracter ao ultimo - retira o \
            answer = ""
            # print("data: ", data)

            if data.count(' ') == 0:
                command = data
                command = command.upper()  # transforma tudo em caixa alta
                print("[INFO] command: " + command)
                # print("sem argumento passado")
                if command == "HELP":
                    answer = help("")
                elif command == "DATAHORA":
                    answer = dataHora()
                elif command == "DEVS":
                    answer = devs()
                elif command == "WEATHER":
                    answer = "[HELP] O comando \weather necessita de uma cidade como argumento. \help weather para saber mais"

                elif command == "WEATHERWEEK":
                    answer = "[HELP] O comando \weatherweek necessita de uma cidade como argumento. \help weatherweek para saber mais"
                else:
                    answer = "[ERROR] Comando inválido. Digite \help para saber mais"
            else:
                command = data.split(" ")[0]  # divide a string em espacos e pega o primeiro elemento
                argument = data.split(command + " ")[1]  # pega o restante da string, retirando o comando+space
                command = command.upper()  # transforma tudo em caixa alta
                print("comando: '" + command + "' argumento: '" + argument + "'")
                if command == "HELP":
                    answer = help(argument)
                elif command == "WEATHER":
                    answer = weather(argument)
                elif command == "WEATHERWEEK":
                    answer = weatherWeek(argument)
                elif command == "DATAHORA":
                    answer = "[HELP] O comando \datahora nao necessita de um argumento"
                elif command == "DEVS":
                    answer = "[HELP] O comando \devs nao necessita de um argumento"
                else:
                    answer = "[ERROR] Desculpe nao reconheci o comando '" + command + "'. Digite \help para saber mais"

            client.send(str(answer).encode())  # envia a resposta para o cliente, depois de processada pelo server
            print("[INFO] Resposta processada e enviada para cliente " + str(endereco[0]) + ":" + str(endereco[1]))
        else:
            answer = data
            client.send(str(answer).encode())  # envia para o cliente mesma coisa que ele mandou pois não é comando
            print("[ERROR] Mensagem de cliente não é um comando, reenviada mesma mensagem para cliente")

    print("[LOG] Thread com cliente finalizada!")


# laco principal do servidor
while True:
    client, endereco = server.accept()  # aceita conexão dos clientes
    threading.Thread(target=conecta, args=(client, endereco)).start()

