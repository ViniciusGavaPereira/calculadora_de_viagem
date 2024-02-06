from Membro import Membro

def busca(nome, lista):
    return [x for x in lista if x.nome == nome]


def gerador_lista(lista) -> list:
    x = [Membro(pessoa) for pessoa in lista]
    return x


def pegar_nome(nome_procurado, lista) -> int:
    for index, dicionario in enumerate(lista):
        if 'Nome' in dicionario and dicionario['Nome'] == nome_procurado:
            print("Encontrado:", dicionario)
            return index
        
        
def adicionarValor(Membro, dic):

        
        'nome = list(test.values())[0]'        
        index_encontrado = pegar_nome(dic['Nome'],Membro.receber)
        print("Encontrado: " , index_encontrado)

        if(index_encontrado != None):
            print("Existe")
            Membro.receber[index_encontrado]['Valor'] = Membro.receber[index_encontrado]['Valor'] + dic['Valor']
        else:
            print('NÃO EXISTE')
            Membro.receber.append(dic)


        