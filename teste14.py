# Escreva um programa que converta uma temperatura digitada 
# em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Qual a temperatura? (Celsius):'))
fahrenheit = (celsius * 9 / 5) + 32
kelvin = (celsius + 273.15)
print(f'equivale à {fahrenheit} graus fahrenheit')
print(f'equivale à {kelvin} graus kelvin')
# f é outra maneira de usar o .format
