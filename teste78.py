# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
print('Digite numeros diferentes:')
valor0 = int(input('Digite um valor para a posição 0: '))
valor1 = int(input('Digite um valor para a posição 1: '))
valor2 = int(input('Digite um valor para a posição 2: '))
valor3 = int(input('Digite um valor para a posição 3: '))
valor4 = int(input('Digite um valor para a posição 4: '))
lista = [valor0, valor1, valor2, valor3, valor4]
maior = max(lista)
menor = min(lista)
print(f'Você digitou os valores {lista}')
for c in lista:
    if maior in lista:
        print(f'O maior valor digitado foi: {maior} na posição {lista[maior]}')
        break
if menor in lista:
    print(f'O menor valor digitado foi: {menor} na posição {lista[menor]}')        
# Este programa so serve para a primeira occorrencia do maior e do menor valor