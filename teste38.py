# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
n1 = int(input('primeiro valor:'))
n2 = int(input('segundo valor:'))
if n1>n2:
    print('Primeiro valor maior.')
elif n1==n2:
    print('Valores iguais')
if n1<n2:
    print('Primeiro valor menor')
