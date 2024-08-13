def aumentar(preco=0,taxa=0,formato=False):
    resposta = preco + (preco * taxa / 100)
    return resposta if formato is False else moeda(resposta)


def diminuir(preco=0,taxa=0,formato=False):
    resposta = preco - (preco * taxa / 100)
    return resposta if formato is False else moeda(resposta)


def dobro(preco=0,formato=False):
    resposta = preco * 2
    return resposta if formato is False else moeda(resposta)


def metade(preco=0,formato=False):
    resposta = preco / 2
    return resposta if formato is False else moeda(resposta)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0,aumento=10,reducao=10):
    print(f'Preço analisado:\t{moeda(preco)}')
    print(f'Dobro do preço: \t{moeda(dobro(preco))}')
    print(f'Metade do preço:\t{moeda(metade(preco))}')
    print(f'{aumento}% de aumento: \t{(aumentar(preco,aumento,True))}')
    print(f'{reducao}% de desconto:\t{(diminuir(preco,reducao,True))}')
