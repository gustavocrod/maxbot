# Introdução
O Teste de Turing foi desenvolvido por Alan Turing em 1950. O teste resume-se em: para uma máquina passar no Teste de Turing, ela deve exibir um comportamento inteligente indistinguível do comportamento de um ser humano.
Apesar de vários estudos terem sidos realizados acerca desse problema, as máquinas capazes de alcançar o sucesso no Teste de Turing são raras. No entanto, não ser capaz de passar estritamente no Teste de Turing não significa que esses sistemas chatbots são inúteis.

Chatbots atuais como Alexa e Siri mostram que eles são capazes de lidar com várias tarefas como atender chamadas, realizar pedidos de comida, responder perguntas, entre outros. Com isso, não propomos um chatbot para se assemelhar a um assistente virtual das gigantes Amazon ou Apple, como mencionadas, nem tampouco passar no Teste de Turing, mas um bot capaz de comunicar-se com serviços de metereologia e atender (de forma automática) a requisições básicas.

### Objetivo Geral
Implementar o M(etereologista) A(utomatizado) X, um \textit{chatbot} que informe a temperatura atual de uma localização e também a previsão para uma semana deste local.

### Objetivos Específicos
  ##### - Entender o funcionamento da API do AccuWeather 
  ##### - Implementar o Servidor do M.A.X
  ##### - Implementar o Cliente do M.A.X que se comunica com o Servidor do M.A.X
  ##### - Acessar o AccuWeather utilizando o servidor do chatbot para informar a previsão do tempo para o Cliente

### Metodologia
Para a implementação do M.A.X, será utilizada a linguagem de programação Python \cite{python} em sua versão 3, a comunicaçao entre o cliente e o servidor, serão utilizados \textit{sockets} (que permitem a comunicação entre processos através de portas distintas, estejam eles na mesma máquina, ou em máquinas diferentes). 
Objetivamos desenvolver as seguintes funcionalidades:

  ##### dev
  Comando que informa o nome dos desenvolvedores do M.A.X

  ##### weather
  Comando que recebe uma cidade como parâmetro, e retorna a temperatura atual da cidade   \\

  ##### Weather week
  Comando que recebe uma cidade como parâmetro, e retorna a previsão do tempo em uma semana da mesma.

As funções a serem implementadas pretendem responder ao usuário sobre temperatura atual e da semana, servindo não somente como na organização pessoal para cada usuário que reside ou pretende estar na cidade pesquisada com para tantas outras utilidades que possam necessitar saber da previsão do tempo.
