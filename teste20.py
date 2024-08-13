# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
print('Sorteio da ordem, fale os nomes:')
aluno1 = input('Nome do primeiro aluno:')
aluno2 = input('Nome do segundo aluno:')
aluno3 = input('Nome do terceiro aluno:')
aluno4 = input('Nome do quarto aluno:')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem escolhida foi: {}'.format(lista))
