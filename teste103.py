# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido # informado corretamente.
def jogador(a=0,b=0):
    a = str(input('Qual o seu nome?'))
    b = str(input('Quantos gols você fez?'))
    if a == '':
        print('Jogador desconhecido')
    else:
        print(f'Jogador {a}')
    if b == '':
        print('Você fez ? gols')
    else:
        print(f'Você fez {b} gols')


jogador()