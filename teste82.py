# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
valores = []
valores2 = []
valores3 = []
while True:
    valores.append(int(input('Digite numeros: ')))
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
for c, v in enumerate(valores):
    if v % 2 == 0:
        valores2.append(v)
    else:
        valores3.append(v)
print(f'A lista completa é {valores}')
print(f'Os numeros pares da lista são {valores2}')
print(f'Os numeros impares da lista são {valores3}')