# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
print ('A ordem de apresentação sera:')
aluno1 = input('Nome do primeiro aluno:')
aluno2 = input('Nome do segundo aluno:')
aluno3 = input('Nome do terceiro aluno:')
aluno4 = input('Nome do quarto aluno:')
lista = [aluno1, aluno2, aluno3, aluno4] 
escolhido =random.choice(lista)
print('Ganhador: {}'.format(escolhido))
