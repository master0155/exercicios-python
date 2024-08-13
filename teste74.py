# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import numbers
import random
numero = random.randint(0,100)
numero1= random.randint(0,100)
numero2= random.randint(0,100)
numero3= random.randint(0,100)
numero4= random.randint(0,100)
tupla = (numero,numero1,numero2,numero3,numero4)
print(numero,numero1,numero2,numero3,numero4)
print(f'O maior numero é {max(tupla)} e o menor numero é {min(tupla)}')
