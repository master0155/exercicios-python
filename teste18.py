# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
import math
print('Valor do seno, cosseno e tangente de um ângulo.')
angulo= float(input('digite o angulo que você deseja:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o seno de {:.4f}'.format(angulo,seno))
print('O angulo de {} tem o cosseno de {:.4f}'.format(angulo,cosseno))
print('O angulo de {} tem o tangente de {:.4f}'.format(angulo,cosseno))
# {:.4f} é o numero de casas decimais apos o a resposta se for um numero decimal.
