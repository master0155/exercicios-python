# Crie um programa que faça o computador jogar Jokenpô com você.
import random
print('Suas escolhas para a jogo de jokenpô:')
print('[ 1 ] Pedra')
print('[ 2 ] Papel')
print('[ 3 ] Tesoura')
computador = random.randint(1,3)
escolha = int(input('sua jogada: '))
if escolha == 1:
    if computador == 1:
        print('Empate')
    elif computador == 2:
        print('Computador ganhou')
    else:
        print('Você ganhou')
elif escolha == 2:
    if computador == 2:
        print('Empate')
    elif computador == 1:
        print('Jogador ganhou')
    else:
        print('Computador ganhou')
elif escolha == 3:
    if computador == 1:
        print('Computador ganhou')
    elif computador == 2:
        print('Jogador ganhou')
    else:
        print('Empate')
else:
    print('Jogada invalida seu burro')
print('jogada do computador: {} '.format(computador))
print('Game Over')
