import json
import pandas as pd 
from Membro import Membro

'Importação da base de dados'
url = 'C:/Users/vini-/Downloads/FinancasViagem.xlsx'
db = pd.read_excel(url, sheet_name='balanco')




Felps = Membro('Felipe',[{'Amanda':30}])

'Cria uma lista de objetos com os membros '

'Pessoas que participaram da viagem:'
membros = list(db.keys())
membros.remove('Pagante')
membros.remove('Valor')
membros.remove('Compra')

'Quem pagou por certo item:'
compras = pd.DataFrame(db[membros])

'Cria uma coluna com o valor a ser pago'

db['Valor_para_pagar'] = round(db['Valor'] / compras.sum(axis='columns'),2)
print(db['Valor_para_pagar'][0])

capturador = db[membros[1]]
'Percorre a coluna'
loop = 4
loop2 = 0
membroAtual = ''


while(loop < len(db.axes[1])):
    membroAtual = membros[loop - 4]
    pagamento = 0

    "print('Membro atual: ' + membroAtual)"
    print(f'Membro atual: {membroAtual}')

    while(loop2 < len(db.iloc[:,:loop2])):
            celula = db.at[loop2,membroAtual]
            recebedor = db.at[loop2,'Pagante']
                    
            if (celula == 1) & (membroAtual != recebedor):
             print("Quem vai pagar: ", membroAtual)
             print("Quem vai receber: ", recebedor)   
             pagamento = pagamento + db['Valor_para_pagar'][loop2]
        
            loop2 = loop2 + 1
    
    print(f'Valor total de {membroAtual}: {round(pagamento,2)}') 
    

    'print(db.iloc[:,:loop])'
    loop2 = 0
    loop = loop + 1


'Compara o nome do header da lista, com o comprador'
'-Caso seja igual, ele pula'
'-Caso seja diferente, ele acrescenta na lista do comprador:'
'--Nome da pessoa: valor a receber'
'Pula para outra coluna'
'Repete o processo'