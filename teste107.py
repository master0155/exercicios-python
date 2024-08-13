# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import teste107.moeda
# from teste107 import moeda
preco = float(input('Digite o preco:'))
print(f'A metade de {preco} é {teste107.moeda.metade(preco)}')
print(f'O dobro de {preco} é {teste107.moeda.dobro(preco)}')
print(f'Aumentando em 10% temos: {teste107.moeda.aumentar(preco,10)}')
print(f'Diminuindo em 10% temos: {teste107.moeda.diminuir(preco,10)}')
# teste107 é o nome da pasta com o arquivo moeda.
