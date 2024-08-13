# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.
numero = (input('informe um numero:'))
# unidade = numero // 1 % 10
# dezena  = numero // 10 % 10
# centena = numero // 100 % 10
# milhar  = numero // 1000 % 10
print('Seu numero tem: {} unidades'.format(numero[3]))
print('Seu numero tem: {} dezenas'.format(numero[2]))
print('Seu numero tem: {} centenas'.format(numero[1]))
print('Seu numero tem: {} milhares'.format(numero[0]))

