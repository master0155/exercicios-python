# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior=0
menor=0
for c in (1,2,3,4,5):
    peso = float(input('Peso da pessoa {}:'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print('O maior peso foi de {}kg'.format(maior))
print('O menor peso foi de {}kg'.format(menor))
