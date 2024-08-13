import math
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
comprimento1= float(input('Qual o comprimento do cateto oposto? '))
comprimento2= float(input('Qual o comprimento do cateto adjacente? '))
total = math.hypot(comprimento1, comprimento2)
print('O comprimento da hipotenusa é: {:.2f}'.format(total))
