# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.
numero1 = int(input('Primeiro valor:'))
numero2 = int(input('Segundo valor:'))
numero3 = int(input('Terceiro valor:'))
if numero1<numero2 and numero1<numero2:
    menor = numero1
if numero2<numero1 and numero2<numero3:
    menor = numero2
if numero3<numero1 and numero3<numero2:
    menor = numero3
if numero1>numero2 and numero1>numero2:
    maior = numero1
if numero2>numero1 and numero2>numero3:
    maior = numero2
if numero3>numero1 and numero3>numero2:
    maior = numero3
print('O maior numero é {} e o menor numero é {}'.format(maior,menor))
