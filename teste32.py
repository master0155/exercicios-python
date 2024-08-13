# Faça um programa que leia um ano qualquer
# e mostre se ele é bissexto.
ano = int(input('Qual o ano? '))
if ano % 2 == 0 and ano % 100 == 1:
    print('Ano bissexto')
else:
    print('Não é bissexto')
