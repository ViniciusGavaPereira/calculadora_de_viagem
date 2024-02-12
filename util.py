from sys import displayhook
from Membro import Membro
import pandas as pd 

def busca(nome, lista):
    return [x for x in lista if x.nome == nome]

def busca_dividas(list, nome):
    
    z = [x for x in list if x['Nome'] == nome]

    if z != []:
        return z[0]['Valor'] 
    else:
        return 0  



def gerador_lista(lista) -> list:
    x = [Membro(pessoa) for pessoa in lista]
    return x

def gerador_lista_2(lista) -> list:
    x = [pessoa for pessoa in lista]
    return x

def objeto_para_lista_nome(lista) -> list:
    x = [pessoa.nome for pessoa in lista]
    return x


def objeto_para_lista_recebedor(lista) -> list:
    x = [x.receber for x in lista]
    return x


def criador_de_linhas(lista,dt):
    pagantes = gerador_lista_2(lista)
    'print(vars(lista[0].receber[0]))'
    'print(dt[0])'
    print("DT",dt)
    for x in range(len(lista)):
     
     nova_linha = [pagantes[x].nome]

     y = 1
     for y in range(len(dt)):
         
      
      nova_linha.append(criador_de_celula(pagantes[x],dt))

      y + 1
     'dt = pd.concat(lista[x].nome,columns=df.columns)'


def criador_de_celula(membro,dt) -> int:

    linha_vazia = []    
    receber = membro.receber
    x = 0

    print("Membro: " , vars(membro))

    
    while (x < dt.size):
        
        quanto_vai_pagar = busca_dividas(receber,dt[x + 1][0])
        
        if dt[x + 1][0] != membro.nome:


            
            print('Pagante: ' , quanto_vai_pagar)

            if(quanto_vai_pagar == None):
                quanto_vai_pagar = 0
        else: 
            quanto_vai_pagar = 0
            

        linha_vazia.append(quanto_vai_pagar)
        x += 1   
         
   

    return linha_vazia


def criar_dataframe(lista,membros) -> list:
    
    cabecalho = ['Pagadores:']

    'Cria o cabeçalho'
    for x in range(len(membros)):
        cabecalho.append(membros[x])

    df = pd.DataFrame(cabecalho).T

   
    df_completa = criador_de_linhas(lista,df)

    print(df_completa)
    ''' 
    recebedores = membros
    dados = criador_de_linhas(lista)
    ''' 
    
"""
    "print(lista[2].receber[0]['Valor'])"
    dt = pd.DataFrame(columns = dataframe)
    print(dt)
    "criador_de_linhas(lista,dt)"

"""
    
    

    
        


        