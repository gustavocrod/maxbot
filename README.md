# M.A.X

![MAX](images/max.png)

## Contexto histórico

O Teste de Turing foi desenvolvido por Alan Turing em 1950. O teste resume-se em: para uma máquina passar no
Teste de Turing, ela deve exibir um comportamento inteligente indistinguível do comportamento de um ser humano.
Apesar de vários estudos terem sidos realizados acerca desse problema, as máquinas capazes de alcançar o sucesso no
Teste de Turing são raras. No entanto, não ser capaz de passar estritamente no Teste de Turing não significa que esses
sistemas chatbots são inúteis.

Chatbots atuais como Alexa e Siri mostram que eles são capazes de lidar com várias tarefas como atender chamadas,
realizar pedidos de comida, responder perguntas, entre outros. Com isso, não propomos um chatbot para se assemelhar a
um assistente virtual das gigantes Amazon ou Apple, como mencionadas, tampouco passar no Teste de Turing,
mas um bot capaz de comunicar-se com serviços de metereologia e atender (de forma automática) a requisições básicas.

---
## Instalação

Instale as dependências utilizando:

```bash
$ pip3 install -r requirements.txt
```

---
## Uso

O código possui 2 instâncias:

| Tipo de Instância       | Como Funciona   | Como iniciar  |
| ------------- |:-------------:| :-----:|
| Servidor Max      | Instancia que executará o servidor MAX | ```$ python3 max.py --ip <IP> --port <Porta> ``` |
| Cliente      | Instancias que executarao clientes que comunicam com o max      |   ```$ python3 client.py --ip <HOST_IP> --port <Porta> ``` |

---
### Comandos

Como um cliente, é possivel utilizar os seguintes comandos:

| Comando        | Sobre   | Sintaxe  |
| ------------- |:-------------:| :-----:|
| datahora     | Informa a data e hora atual | ```$ \datahora ``` |
| devs     | Mostra informacoes sobre os desenvolvedores do MAX | ```$ \devs ``` |
| weather     | Espera uma cidade como parâmetro e retorna a temperatura atual desta localização. | ```$ \weather <cidade> ``` |
| weatherweek     | Espera uma cidade como parâmetro e retorna a respectiva previsão do tempo num periodo de 5 dias. | ```$ \weatherweek <cidade> ``` |
| help     | Informa os comandos disponíveis, ou mais informações sobre determinado comando | ```$ \help ``` ou ```$ \help <comando> ``` |

---

