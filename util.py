from Membro import Membro

def busca(nome, lista):
    return [x for x in lista if x.nome == nome]


def gerador_lista(lista) -> list:
    x = [Membro(pessoa) for pessoa in lista]
    return x


def pegar_nome(nome_procurado, lista) -> bool:
    for index, dicionario in enumerate(lista):
        if 'Nome' in dicionario and dicionario['Nome'] == nome_procurado:
            print("Encontrado:", dicionario)
            return index
        
        
def adicionarValor(Membro, dic):

        
        'nome = list(test.values())[0]'        
        
        print("Vamos ver isso aqui SELF: " , pegar_nome(dic['Nome'],Membro.receber))
        print("Vamos ver isso aqui DIC[NOME]: " , dic['Nome'])

        for dic['Nome'] in Membro.receber:
        
            '''
                print("NOME: ", list(dic['Nome'])[0])
            print('EXISTE')
            print("Dicionario novo", dic)
            print('Dicionario existente',  self.receber)
            print('Valor puro: ',  self.receber[0]['Valor'])
            '''
            Membro.receber[0]['Valor'] = Membro.receber[0]['Valor'] + dic['Valor']
            break

        else:
            print('NÃO EXISTE')
            Membro.receber.append(dic)


        