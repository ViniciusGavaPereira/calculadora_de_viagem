from Membro import Membro


def busca(nome, lista):
    return [x for x in lista if x['receber'] == nome]


def gerador_lista(lista) -> list:
    x = [Membro(pessoa) for pessoa in lista]
    return x
