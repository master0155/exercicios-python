# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
sair = 1
media = 0
qntdnumeros = 0
soma = 0
while sair != 0:
    n1 = int(input('Digite um numero: '))
    qntdnumeros += 1
    soma += n1
    media = soma / (qntdnumeros )
    if qntdnumeros == 1:
        maior = n1
        menor = n1
    else:
        if n1>maior:
            maior=n1
        if n1<menor:
            menor=n1
    sair = int(input('Deseja sair digite 0: '))
else:
    print('A media do numero é', media)
    print('O maior e o menor numero é', maior, 'e', menor)

