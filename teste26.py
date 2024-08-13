# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra
# "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
nome = input('Digite um nome: ').strip()
print('A letra A aparece: {}'.format(nome.count('a')))
print('A primeira letra A aparece: {}'.format(nome.find('a')))
print('A ultima letra A aparece: {}'.format(nome.rfind('a')))
