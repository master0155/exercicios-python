# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = input('Deseja continuar? (sim ou não): ').strip()
    if continuar == 'não':
        break
print(lista)
while True:
    opcao = int(input('Deseja ver as nostas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('Fim')
        break
    elif opcao <= len(lista) -1:
        print(f'Notas de {lista[opcao][0]} são {lista[opcao][1]}')
print('Fim.')
