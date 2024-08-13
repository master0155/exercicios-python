# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

continuar = 0
count = 0
total = 0
count1 = 0
menor = 0
barato = ''
while continuar != 'N':
    nome = input('nome do produto: ')
    preço = float(input('preço: R$'))
    total += preço
    count1 += 1
    if count1 == 1:
        menor = preço
        barato = nome
    else:
        if preço <= menor:
            menor = preço
    if preço >= 1000.00:
        count += 1
    continuar = input('continuar? [S/N]').upper()
print(f'O total da compra foi R${total}', end = '')
print(f'O produto mais barato foi {nome}, com preço {menor} e o', end = '')
print(f'O total de produtos foi {count1}')
    