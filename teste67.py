# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    numero = int(input('Numero da tabuada:'))
    for c in range(0,11):
        print(f'{numero} x {c} = {numero*c}')
    continuar = int(input('Digite um numero de valor negativo para parar:'))
    if continuar <= 0:
        break