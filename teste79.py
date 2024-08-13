# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
continuar = 'sim'
num = list()
while continuar == 'sim':
    numero = (input('Digite um numero: '))
    if numero not in num:
        num.append(numero)
    else:
        print('Valor duplicado, não adicionado a lista')
    continuar = input('Deseja continuar, sim ou não? ')
num.sort
print(num)