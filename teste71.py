# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
continuar = 'S'
while continuar == 'S':
    valor = int(input('Qual o valor a ser sacado? '))
    nota50 = valor // 50
    valor %= 50
    nota20 = valor // 20
    valor %= 20
    nota10 = valor // 10
    valor %= 10
    nota01 = valor // 1
    valor %= 1
    print(f'notas de 50 = {nota50}')
    print(f'notas de 20 = {nota20}')
    print(f'notas de 10 = {nota10}')
    print(f'notas de 01 = {nota01}')
    continuar = input('Deseja continuar? [S/N]').upper()
