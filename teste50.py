# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
print('digite 6 numeros inteiros e sera mostrado a soma dos numeros pares')
for c in range(1,7): 
    n1 = int(input('Digite 6 valores com numeros inteiros:'))
    if n1 % 2 == 0:
        soma = n1 + soma
print(soma)