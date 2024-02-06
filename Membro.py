class Membro():
    def __init__(self,nome) -> None:
        self.nome = nome
        self.receber = []

    def adicionarValor(self, dic):

        if dic in self.receber:
            print("Dicionario já existe")
            print('Dicionario existente',  self.receber)
        else:
            self.receber.append(dic)
            print('Dicionario não existe')    



