from sys import displayhook
from Membro import Membro
import pandas as pd 

def busca(nome, lista):
    return [x for x in lista if x.nome == nome]


def gerador_lista(lista) -> list:
    x = [Membro(pessoa) for pessoa in lista]
    return x

def objeto_para_lista_nome(lista) -> list:
    x = [pessoa.nome for pessoa in lista]
    return x


def objeto_para_lista_recebedor(lista) -> list:
    x = [x.nome for x in lista]
    return x


def objeto_para_lista_recebedor2(lista) -> list:
    x = [x.nome for x in lista]
    y = [y.receber for y in lista]
    return {x, y}

def criador_de_linhas(lista,index) -> set:
    
    x = [objeto_para_lista_recebedor(dado,index) for dado in lista]
    print(x)
    return {x}

def criar_dataframe(lista,membros) -> list:
    pagantes = objeto_para_lista_nome(lista)
    ''' 
    recebedores = membros
    dados = criador_de_linhas(lista)
    ''' 
    print(objeto_para_lista_recebedor(lista))
    "print(lista[2].receber[0]['Valor'])"
    dt = pd.DataFrame(columns = pagantes)
    
    

    
        


        