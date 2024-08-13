def aumentar(preco,taxa):
    resposta = preco + (preco * taxa / 100)
    return resposta


def diminuir(preco,taxa):
    resposta = preco - (preco * taxa / 100)
    return resposta


def dobro(preco):
    resposta = preco * 2
    return resposta


def metade(preco):
    resposta = preco / 2
    return resposta


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')
