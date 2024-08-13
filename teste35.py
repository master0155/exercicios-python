# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
primeiro = float(input('Primeiro segmento:'))
segundo = float(input('Segundo segmento:'))
terceiro = float(input('Terceiro segmento:'))
if primeiro + segundo>terceiro and segundo+terceiro>primeiro and terceiro+primeiro>segundo:
    print('Forma um triangulo')
else:
    print('Não forma um triangulo')

