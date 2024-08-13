# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.
algo = (input('digite algo:'))
print('Tipo primitivo:',type(algo))
print('Só tem espaços:',algo.isspace())
print('Só tem números:',algo.isnumeric())
print('É uma letra?:',algo.isalpha())
print('É uma letra ou numero:',algo.isalnum())
print('Esta só em maiusculas:',algo.isupper())
print('Esta só em minusculas:',algo.islower())
