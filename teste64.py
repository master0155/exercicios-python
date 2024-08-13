# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n1 = count = 0
soma = 0
while n1!= 999:
    n1 = int(input('Advinhe um numero: '))
    if n1 == 999:
        soma -= 999
    soma += n1
    count += 1
print(f'A soma foi {soma}')
print('Fim')
