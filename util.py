from sys import displayhook
from Membro import Membro
import pandas as pd 

def busca(nome, lista):
    return [x for x in lista if x.nome == nome]


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

    for x in range(len(lista)):
     nova_linha = {'Pagadores:': pagantes[x].nome, str(dt[x+1]) : criador_de_celula(pagantes[x],dt[x+1])}

     'dt = pd.concat(lista[x].nome,columns=df.columns)'


def criador_de_celula(membro,dt) -> int:
    print('Entrou nessa porra')
    print(vars(membro))
    return 1

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
    
    

    
        


        