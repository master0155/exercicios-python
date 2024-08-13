# Faça um programa que calcule a soma entre todos os números que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.
print('soma entre todos os números impares que são múltiplos de três')
for c in range(0,50):
    if c % 2 == 1 and c % 3 == 0:
        print(c)
