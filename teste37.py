# Escreva um programa em Python que leia um número inteiro qualquer e peça para o 
# usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
n1 = int(input('Fale um numero inteiro:'))
escolha = int(input('print deseja transformar {} em valor 1 (binario), 2 (octal), ou 3 (hexadecimal?)'.format(n1)))
if escolha == 1:
    binario = bin(n1)
    print(binario)
elif escolha == 2:
    octal = oct(n1)
    print(octal)
if escolha == 3:
    hexadecimal = hex(n1)
    print(hexadecimal)
