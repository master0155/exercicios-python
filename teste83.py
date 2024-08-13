# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
lista = []
count = 0
count1 = 0
conta = input('Digite a axpressão: ')
for c in conta:
    if conta == '(':
        count += 1
    elif conta == ')':
        count1 += 1
    if count == count1:
        print('Conta valida.')
    else:
        print('Conta invalida.')
    break