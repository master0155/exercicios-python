# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
par = list()
impar = list()
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor:'))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
par.sort()
impar.sort()
print(f'Os valores pares digitados foram:{par}')
print(f'Os valores impar digitados foram:{impar}')
