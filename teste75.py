# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
count = 0
par = 0
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))
numero4 = int(input('Digite um numero: '))
numero5 = int(input('Digite um numero: '))
tupla = (numero1,numero2,numero3,numero4,numero5)
print(f'Voce digitou os valores {tupla}')
for c in tupla:
    if c == 9:
        count += 1
    if c % 2 == 0:
        par+=1
print(f'Quantidade de vezes que apareceu o numero 9: {count}')
print(f'O valor tres apareceu na posicao {tupla.index(3)}')
print(f'Quantas vezes teve numeros pares {par}')
