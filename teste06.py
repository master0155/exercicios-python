# Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada.
n1 = float(input('fala um numero:'))
rq = n1 ** (1/2)
print('o dobro desse numero é {}'.format(n1 * 2))
print('o triplo desse numero é {}'.format(n1 * 3))
print('a raiz quadrada desse numero é {}'.format(round(rq,2)))
# round é para delimitar a quantidade de casas decimais, em um numero decimal(round) (,2).
