# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
import time
sair_do_programa = 5
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != sair_do_programa:
    print('Opção [1] (somar)')
    print('Opção [2] (multiplicar)')
    print('Opção [3] (maior)')
    print('Opção [4] (novos numeros)')
    print('Opção [5] (sair do programa)')
    opcao = int(input('Escolha uma das opções para seus valores:'))
    if opcao == 1:
        somar = n1+n2
        print('A soma dos valores é igual a', somar)
    elif opcao == 2:
        multiplicar = n1 * n2
        print('A multiplicação dos valores é igual a', multiplicar)
    elif opcao == 3:
        if n1 > n2:
            print('O numero maior é',n1)
        else:
            print('O numero maior é',n2)
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
else:
    print('Fim do programa')
