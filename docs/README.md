# Documentação do M.A.X

## M.A.X client

#### client.main()
Função principal do programa do lado do cliente

#### client.makeConnection(host, port)
Função responsável por estabelecer a conexao com o servidor

* **Parametros**
    * **host** – Endereço Ip que o servidor do max está rodando
    * **port** – Porta em que o servidor esta rodando

#### client.clientHandler(server):
Funcao manipuladora, onde acontece toda a lógica do cliente

* **Parametros**
    * **server** –  objeto socket responsavel pela conexao com o servidor
    
 
## M.A.X max

#### max.main()
Função principal do programa do lado do servidor do max

#### max.runServer(ip, port)
Função responsável pela inicialização do servidor e de criar conexões com cada cliente

* **Parametros**
    * **ip** – Endereço Ip que o servidor do max rodará
    * **port** – Porta em que o servidor rodará

#### max.makeConnection(client, endereco)
Função que roda em cada thresh, responsável por cada conexao de um cliente

* **Parametros**
    * **client** – socket responsável pela conexão com o cliente
    * **endereco** – tupla que contem o ip e porta do cliente em questão
    
## M.A.X commands

#### commands.devs()
Função que retorna os nomes dos desenvolvedores

* **Retorno**
   * **answer** - uma string contendo os nomes dos desenvolvedores
  
#### commands.dataHora()
Função que solicita o horario local da máquina

* **Retorno**
   * **answer** - uma string contendo o horário atual

#### commands.help(argument):
Função que retorna lista de comandos disponíveis ou mais informações sobre algum comando

* **Parametros**
    * **argument** – string que representa o comando que se deseja obter mais informações
    
* **Retorno**
   * **answer** - string com os comandos disponíveis ou com mais informações sobre um comando
   
#### commands.weather(argument):
Função que requisita ao serviço de metereologia, via request http (GET) e retorna informações sobre o clima atual da cidade requisitada
* **Parametros**
    * **argument** – string que é a cidade a ser pesquisada
    
* **Retorno**
   * **answer** - condição climatica atual da localização ou uma mensagem de erro caso a cidade não tenha sido informada
   
#### commands.weatherWeek(argument)
Função que recebe uma cidade como parametro, e requisita ao serviço de metereologia, via request http (GET) e retorna a previsão do tempo para ela, no período de uma semana

* **Parametros**
    * **argument** – strubg que representa a cidade a ser pesquisada
    
* **Retorno**
   * **answer** - previsão do tempo de uma semana para a cidade pesquisada


