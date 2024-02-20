from sys import displayhook
from Membro import Membro
import pandas as pd 
import numpy as np

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


def gerador_cabecalho(membros) -> list :
    cabecalho = ['Pagadores:']

    'Cria o cabeçalho'
    for x in range(len(membros)):
        cabecalho.append(membros[x])

    return cabecalho


def criador_de_linhas(lista,dt):
    pagantes = gerador_lista_2(lista)


    dados = [gerador_cabecalho(objeto_para_lista_nome(pagantes))]

    for x in range(len(lista)):
     
     nova_linha = [pagantes[x].nome]

     for y in range(len(dt)):
         
      
      nova_linha = criador_de_celula(nova_linha, pagantes[x],dt)

              
      teste = list(nova_linha)
      dados.append(teste)
      
    return dados


      



def criador_de_celula(linha,membro,dt) -> int:

    nova_linha = linha    
    receber = membro.receber
    x = 0

    while (x + 1 < len(dt.columns)):
        
        quanto_vai_pagar = busca_dividas(receber,dt.iloc[0, x + 1])
        
        if dt[x + 1][0] != membro.nome:

            if(quanto_vai_pagar == None):
                quanto_vai_pagar = 0
        else: 
            quanto_vai_pagar = 0
            

        nova_linha.append(quanto_vai_pagar)
        x += 1   
         
   

    return nova_linha


def criar_dataframe(lista,membros) -> list:
    
    cabecalho = gerador_cabecalho(membros)

    df = pd.DataFrame(cabecalho).T

   
    df_completa = criador_de_linhas(lista,df)
    return df_completa

  


        