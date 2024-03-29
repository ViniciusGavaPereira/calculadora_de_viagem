class Membro():
    def __init__(self,nome) -> None:
        self.nome = nome
        self.receber = []

    def pegar_nome(self,nome_procurado) -> int:
        for index, dicionario in enumerate(self.receber):
            if 'Nome' in dicionario and dicionario['Nome'] == nome_procurado:
                return index
                
    def adicionarValor(self, dic):

        index_encontrado = self.pegar_nome(dic['Nome'])

        if(index_encontrado != None) & (self.nome.strip() != dic['Nome'].strip()):
                self.receber[index_encontrado]['Valor'] = round(self.receber[index_encontrado]['Valor'] + dic['Valor'],2)
        else:
                self.receber.append(dic)

    

