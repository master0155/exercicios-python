# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    nasceu = int(input('Em que ano a pessoa numero {} nasceu ?'.format(c)))
    idade = atual - nasceu
    if idade >=21:
        totmaior += 1
    else:
        totmenor+= 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade.'.format(totmenor))
