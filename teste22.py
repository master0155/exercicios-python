# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
nome = input('Qual o seu nome completo? ')
print('seu nome em maiusculo:',nome.upper())
print('seu nome em minusculo:',nome.lower())
print('total de letras do seu nome:',(len(nome) - nome.count(' ')))
print('total de letras do seu primeiro nome:',nome.find(' '))
