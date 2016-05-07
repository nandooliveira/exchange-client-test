# Coding session

Assumimos uma API onde comparações de moedas estrangeiras acontecem. 
Neste [entry point](http://104.131.152.220:8080/payment-api-v1/currencies/real/exchange-rate/), voce pode visualizar 5 itens retornando no seguinte padrão:

```
[ {
  "vetProvider" : "comercial",
  "symbol" : "$",
  "rate" : 3.5045
}, {
  "vetProvider" : "early adopter",
  "symbol" : "R$",
  "rate" : 3.4169
}, {
  "vetProvider" : "common",
  "symbol" : "R$",
  "rate" : 3.3818
}, {
  "vetProvider" : "cotacao",
  "symbol" : "R$",
  "rate" : 3.3293
}, {
  "vetProvider" : "itau",
  "symbol" : "R$",
  "rate" : 3.2855
} ]
```
Descrição da API:
* VetProvider - Banco provedor da cotação ou cotação comercial oficial do Banco Central
* Symbol - A moeda que foi consultada. 
* Comercial $ (valor consultado em dolar - real no banco central. Cotação comercial); 
* Cotacao (banco cotacao) esta pagando R$ 3.3293 por dolar; 
* Early adopter (banco) esta pagando R$ 3.4169; 
* e o Itau esta pagando R$3.2855 por dolar.


Problema ?!
* Essa API realiza os calculos de cotação "live" para cada request. Isso é bom pois as informações estão sempre atualizadas com o mercado financeiro porem voce sempre ira perder os retornos passados ao realizar um novo trigger.

# Desafio 1
* Voce devera criar uma rotina back-end para realizar um trigger nesta API a cada 2 minutos (configuraveis via parametrização) e salvar o retorno em um banco de dados NoSQL (MongoDB), realizando o storage de um campo datetime, informando o momento em que a consulta foi realizada.

# Desafio 2
- Uma vez que vc possui um histórico de 2 em 2 minutos (720 registros a cada 24 horas) desta API, com data e hora, voce devera expor essa informação do seu back-end (MongoDB) via JSON para ser consumida pelo seu client web (mais abaixo).

# Desafio 3
Agora que o histórico já é acessivel via HTTP/JSON podemos ir além, o que acha?
Usando HTML/CSS e Javascript use a sua imaginação para trabalhar com essas informações. Uma excelente lib é o http://www.chartjs.org/
* PS Funcionalidades e inteligencia dos resultados tera mais valor que layout. Fique sucessagado :)

O que voce pode fazer?

* Gráficos Line Chart comparativo (várias "lines" no mesmo chart) exibindo todos os bancos e a cotação comercial do dia.
* Capacidade de realizar busca por periodo. Voce pode criar validações como a data de inicio sempre sendo maior que a final. Busca máxima de 1 ano e etc ou periodos fixos (1 semana, 1 mes, 1 ano etc). Use o capricho e imaginação para encontrar melhorias faceis de ser implementadas e que levam o resultado o mais próximo possivel de um software a ser usado em produção
* Exibir a variação do dolar comercial em % deste o ultimo dia/semana/mes. i.e https://www.coinbase.com/charts

# Desafio 4:
* Pensando em conceitos como engenharia de software, design patterns e pensando nos nossos próximos amigos que irão continuar esse teste. Quão dificil deverá ser quando essa API incluir um novo banco comparativo de dolar?
* Quão dificil será passar um outro entry point da API que retorna outra moeda (Euro -> Real por exemplo). Seu gráfico é capaz de realizar troca entre moedas?

- Desafio 5
* Como é gerenciado o seu trigger de 2 em 2 minutos? 
* Voce esta criando uma fila? 
* Será um sleep no código por 2 minutos (sounds bad :p)? 
* O que acontece se o servidor cair faltando 30 segundos para o próximo trigger? 
* Seu software ira tentar realizar o trigger em 2:0x minutos caso o servidor volte depois do ultimo trigger ou já era?


# Observações:
 
* Back-end
Podera ser feito nas liguaguens Java, Ruby, Python Ou Javascript (node.js etc). Escolha qual voce tem mais aptdão e produtividade. Acreditamos que a linguagem é apenas uma ferramenta e o bom programador será capaz de migrar entre elas sem maiores problemas.

* Front-end
Sabemos o quanto é dificil para um dev entender de layout, design, css e etc. Porem, nada como bootstrap ou materializecss para nos ajudar nestes casos. O Layout não será decisivo mas tbm não esperamos algo plain HTML. Seja criativo até onde seus dev skills podem te levar :)

* Desafios
É facil perceber que são progressivos em questão e dificuldade, iniciando de algo bem simples como consumir uma API e salvar em um NoSQL até definições de arquitetura. Caso voce consiga realizar todos, excelente. Caso contrário nos explique qual foi a sua dificuldade.

# Shiping the code
* Voce devera submeter um PR para este repositorio até quarta-feira 00:00 BRT.
* Esperamos um README file com sugestões de como rodar o seu projeto. Caso voce queira ir além, um deploy no "Claudio" (heroku like) não seria nada ruim! Isso pode demonstrar proatividade e contar como pontos extras, além de nos salvar um tempinho precioso. :) #ficadica

Boa Sorte.
