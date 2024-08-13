import moeda
preco = float(input('Digite o preço:'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando em 10% temos: {moeda.moeda(moeda.aumentar(preco,10))}')
print(f'Diminuindo em 10% temos: {moeda.moeda(moeda.diminuir(preco,10))}')