# Escreva um programa que leia um número N inteiro qualquer 
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
print('Sequencia de Fibonnacci:')
n1 = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
count = 0
while count <= n1:
    termo3 = termo1 + termo2 
    termo1 = termo2
    termo2 = termo3
    print(termo3)
    count += 1
print('Fim')
