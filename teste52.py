# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n1 = int(input('Digite um numero:'))
multiplo = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('multiplo/divisivel de {}'.format(c))
        multiplo+=1
if multiplo>2:
    print('Não é primo')
else:
    print('É primo')
#numeros primos sao diviseis por 1 e por eles mesmos.