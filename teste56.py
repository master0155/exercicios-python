# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0 
media = 0
maiorIdade = 0
qtdMulher = 0

for count in range(1,5):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo F/M: ')
    soma += idade
    media = soma / count
  
    if (idade > maiorIdade):
        maiorIdade = idade
        nomeVelho = nome 

    if (sexo == 'F' and idade < 20):
        qtdMulher += 1

print('A média das idade é: {}.'.format(media))
print('O nome do mais velho é {}'.format(nomeVelho))
print('Você é mulher e tem menos de 20 anos. Possui {} mulheres.'.format(qtdMulher))
    
