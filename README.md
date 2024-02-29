# Calculadora_de_viagem

Este sistema foi criado pensando em auxiliar amigos a fazerem os calculos dos seus gastos de viagem.

## Base de dados

A base utilizada para consumo, é uma planilha .xlsx que armazena as informações dos gastos da viagem. É importânte que ela mantenha o padrão apresentado a seguir:

A planilha pode ser encontrada neste Github, no caminho: calculadora_de_viagem/dados/BalancoViagem.xlsx

![image](https://github.com/ViniciusGavaPereira/calculadora_de_viagem/assets/74336299/4d95f9eb-b304-4053-a8a0-00bf99279c21)

Coluna laranja: o nome de quem pagou por determinada compra

Coluna azul: o nome da compra

Coluna verde: o valor total do item

Depois destas três colunas, devem ser criadas as colunas cinzas. No topo terá o nome do integrante e em cada linha de produto, deve ser colocado 1 caso ele tenha consumido e 0 caso ele não tenha consumido. 

#### Este padrão deve ser seguido, pois o código espera que a planilha será entregue neste formato

Após rodar o algoritmo, ele irá criar uma nova planilha dentro das pastas do código, no caminho: calculadora_de_viagem/dados/Resultado.xlsx 
![image](https://github.com/ViniciusGavaPereira/calculadora_de_viagem/assets/74336299/47521c4a-4219-4e7e-9333-d15688703ce0)


A primeiro linha azul representa o pagador, e em baixo dele, representa o quanto ele deve pagar para cada pessoa na linha vermelha.

#### Exemplo:
![image](https://github.com/ViniciusGavaPereira/calculadora_de_viagem/assets/74336299/1642a72f-2e86-479a-9af5-2dbc453a1f20)

Fernando deve pagar R$ 38,90 para Felipe


