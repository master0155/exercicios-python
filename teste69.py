# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
print('Cadastro de humanos')
count = 0
continuar = 'S'
homem = 0
mulher = 0
while continuar != 'N':
    idade = int(input('Idade: '))
    sexo = input('genero [M/F]: ').upper()
    continuar = input('Continuar [S/N] ').upper()
    if idade >= 18:
        count += 1
    if sexo == 'M':
       # if idade >= 18:
            homem += 1
    elif sexo == 'F':
        if idade >= 22:
            mulher += 1
print(f'Total de pessoas cadastradas {count}, total de homens {homem}, total de mulheres {mulher}')
    