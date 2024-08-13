# Adapte o código do desafio 107, criando uma função adicional chamada
# moeda() que consiga mostrar os números como um valor monetário formatado.
import teste108.moeda
# from teste108 import moeda
preco = float(input('Digite o preço:'))
print(f'A metade de {teste108.moeda.moeda(preco)} é {teste108.moeda.moeda(teste108.moeda.metade(preco))}')
print(f'O dobro de {teste108.moeda.moeda(preco)} é {teste108.moeda.moeda(teste108.moeda.dobro(preco))}')
print(f'Aumentando em 10% temos: {teste108.moeda.moeda(teste108.moeda.aumentar(preco,10))}')
print(f'Diminuindo em 10% temos: {teste108.moeda.moeda(teste108.moeda.diminuir(preco,10))}')
# teste108 é o nome da pasta com o arquivo moeda.