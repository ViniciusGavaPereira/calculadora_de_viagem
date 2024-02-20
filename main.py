import pandas as pd 
from Membro import Membro
from util import *

'Importação da base de dados'
url = 'C:/Users/vini-/Downloads/FinancasViagem.xlsx'
db = pd.read_excel(url, sheet_name='balanco')

'Lista de pessoas que participaram da viagem:'
membros = list(db.keys())
membros.remove('Pagante')
membros.remove('Valor')
membros.remove('Compra')

'Quem pagou por certo item:'
compras = pd.DataFrame(db[membros])

'Cria uma lista de objetos com os membros da lista atual'
lista_membros = gerador_lista(membros)

'Cria uma coluna com o valor a ser pago'

db['Valor_para_pagar'] = round(db['Valor'] / compras.sum(axis='columns'),2)

'Percorre a coluna'
loop = 4
loop2 = 0
membroAtual = ''


"Percorre as colunas"
while(loop < len(db.axes[1])):
    'Quem deve pagar'
    membroAtual = membros[loop - 4]

    'Percorre as linhas'
    while(loop2 < len(db.iloc[:,:loop2])):
            'Valor que armazena se a pessoa participou ou não da compra'
            celula = db.at[loop2,membroAtual]

            'Valor a pagar'
            Valor_para_pagar = db['Valor_para_pagar'][loop2]

            'Quem vai receber o valor'
            recebedor = db.at[loop2,'Pagante']



            try:
                if (celula == 1) & (recebedor != membroAtual):
                    recebedorAtual = busca(recebedor,lista_membros)[0]
                    recebedorAtual.adicionarValor({'Nome': membroAtual, "Valor": round(Valor_para_pagar,2)})

            except IndexError:
                recebedorAtual = 'null'


            loop2 = loop2 + 1
        

    loop2 = 0
    
    loop = loop + 1

dataframe = criar_dataframe(lista_membros,membros)

final = pd.DataFrame(dataframe)
print(final)

final.to_excel("C:/Users/vini-/Downloads/FinancasViagem.xlsx",sheet_name='resultado',index=False,header=False)


