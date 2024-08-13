# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes
primeiro = float(input('Primeiro segmento:'))
segundo = float(input('Segundo segmento:'))
terceiro = float(input('Terceiro segmento:'))
if primeiro + segundo>terceiro and segundo+terceiro>primeiro and terceiro+primeiro>segundo:
    print('Forma um triangulo')
    if primeiro == segundo != terceiro:
        print('Forma um {}'.format('Isósceles'))
    elif primeiro == segundo == terceiro:
        print('Forma um {}'.format('Equilátero'))
    elif primeiro != segundo != terceiro:
        print('Forma um {}'.format('Escaleno'))
else:
    print('Não forma um triangulo')
