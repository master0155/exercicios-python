# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
import time
def linha():
    print('='*25)
def contagem():
    for c in range(1,11):
        print(c, end = ' ',)
    print('fim')
def contagem2():
    for c in range(10,-1,-2):
        print(c, end = ' ',)
    print('fim')


linha()
print('Contagem de 1 até 10 de 1 em 1.')
contagem()
linha()
print('Contagem de 10 até 0 de 2 em 2.')
contagem2()
linha()
print('Agora é a sua vez de personalizar a contagem')
linha()
inicio = (int(input('Inicio:')))
final = (int(input('Final:')))
passo = (int(input('Passo:')))
for c in range(inicio,final+1,passo):
        print(c, end = ' ',)
print('fim')
#sleep()
