import moeda
preco = float(input('Digite o preço:'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco,True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco,True)}')
print(f'Aumentando em 10% temos: {moeda.aumentar(preco,10,True)}')
print(f'Diminuindo em 10% temos: {moeda.diminuir(preco,10,True)}')