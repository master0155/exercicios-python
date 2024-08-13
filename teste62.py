# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print('razão do numero escolhido:')
n1 = int(input('primeiro termo: '))
n2 = int(input('razão do primeiro valor: '))
termo = n1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(termo), end = '')
        termo += n2
        cont +=1
    print('Pausa')
    mais = int(input('Quantos termos você quer a mais? '))
print('Total de termos:', total)
print('fim')