# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores
# lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for c in range(0,3):
    for d in range(0,3):
        matriz [c][d] = input(f'digite o valor para {c},{d}:')
print(matriz)