# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random
lista = list()
jogos = list()
count = 0
total = 0
quantidade = int(input('Quantos jogos você quer que sejam sorteados? '))
while total < quantidade:
    while True:
        num = random.randint(0,60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear
    total += 1
print(f'Os numeros sorteados foram {jogos}')
