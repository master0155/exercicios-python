# Crie um programa que leia dois números
# e mostre a soma entre eles
n1 = int(input('digite um valor:'))
n2 = int(input('digite mais um:'))
S = n1 + n2
# print('a soma entre os dois valores é igual a:', S) 
# print('a soma entre n1, 'e', n2, 'vale', S)
# Em verde são duas formas menos eficientes de fazer a ultima linha
print('a soma entre {} e {} vale {}'.format(n1, n2, S))
