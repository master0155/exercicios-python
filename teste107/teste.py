import moeda
preco = float(input('Digite o preço:'))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'Aumentando em 10% temos: {moeda.aumentar(preco,10)}')
print(f'Diminuindo em 10% temos: {moeda.diminuir(preco,10)}')