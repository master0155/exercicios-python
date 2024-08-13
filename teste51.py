# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('razão do numero escolhido:')
n1 = int(input('primeiro valor: '))
n2 = int(input('razão do primeiro valor: '))
n3 = n2*10
for c in range(n1,n3,+n2):
    print(c)