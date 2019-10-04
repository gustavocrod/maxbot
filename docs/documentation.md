# Documentação do M.A.X

## M.A.X Client

#### client.main()
Função principal do programa

#### client.MakeConnection(host, port)
Função responsável por estabelecer a conexao com o servidor

* **Parametros**
    * **Host** – Endereço Ip que o servidor do max está rodando
    * **Port** – Porta em que o servidor esta rodando

#### client.clientHandler(server):
Funcao manipuladora, onde acontece toda a lógica do cliente

* **Parametros**
    * **server** –  objeto socket responsavel pela conexao com o servidor
