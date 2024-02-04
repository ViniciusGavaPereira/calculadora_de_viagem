import json
import pandas as pd 
from Membro import Membro

'Importação da base de dados'
url = 'C:/Users/vini-/Downloads/FinancasViagem.xlsx'
db = pd.read_excel(url, sheet_name='balanco')




Felps = Membro('Felipe',100,[{'Amanda':30}])

'Cria uma lista de objetos com os membros '

'Pessoas que participaram da viagem:'
membros = list(db.keys())
membros.remove('Pagante')
membros.remove('Valor')
membros.remove('Compra')

'Quem pagou por certo item:'
compras = pd.DataFrame(db[membros])


'Cria uma coluna com o valor a ser pago'

db['valor_para_pagar'] = round(db['Valor'] / compras.sum(axis='columns'),2)

capturador = db[membros[1]]
'Percorre a coluna'
loop = 4
loop2 = 0
membroAtual = ''


while(loop < len(db.axes[1])):
    membroAtual = membros[loop - 4]
    print('Membro atual: ' + membroAtual)
    print(db.iloc[:,:loop])
    loop = loop + 1

'Compara o nome do header da lista, com o comprador'
'-Caso seja igual, ele pula'
'-Caso seja diferente, ele acrescenta na lista do comprador:'
'--Nome da pessoa: valor a receber'
'Pula para outra coluna'
'Repete o processo'