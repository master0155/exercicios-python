# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite seu nome completo:').strip()
print('Muito prazer em te conhecer')
nome2 = nome.split()
print('Seu primeiro nome é {}'.format(nome2[0]))
print('Seu ultimo nome é {}'.format(nome2[-1]))
