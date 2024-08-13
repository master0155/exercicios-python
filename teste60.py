# Faça um programa que leia um número qualquer e mostre o seu fatorial.
from math import factorial
sair = 0
while sair != 1:
    n1 = int(input('Digite um numero para calcular o seu fatorial: '))
    f = factorial(n1)
    print('O seu fatorial foi', f)
    sair = int(input('Deseja sair? se sim, digite 1:'))
print('Fim')