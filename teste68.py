# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
import random
vitoria = 0
derrota = 0
n1 = count = 0
print('Jogo do par ou impar')
while derrota == 0:
    n1 = int(input('Digite um valor:'))
    dedos = input('[P/I]?')
    computador = random.randint(0,10)
    soma = n1 + computador
    print(f'O jogador jogou {n1} e o computador jogou {computador} dedos, igual a {soma}')
    if soma % 2 == 0:
        if dedos == 'P':
            vitoria += 1
            print('Jogador venceu')
        else:
            print('Jogador perdeu')
    else:
        if dedos == 'I':
            vitoria += 1
            print('Computador perdeu')
        else:
            print('Computador venceu')
            derrota += 1
print(f'O jogador teve {vitoria} vitorias contra o computador')
