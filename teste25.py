# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Qual o seu nome completo?').strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
