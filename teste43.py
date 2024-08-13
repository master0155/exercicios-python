# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))
imc = peso / (altura ** 2)
if imc <= 18.4:
    print('Abaixo do peso, imc <= 18.4')
elif imc <= 25.0:
    print('Peso ideal, imc <= 25.0')
elif imc <= 30:
    print('Sobrepeso, imc <= 30')
elif imc <= 40:
    print('Obesidade, <= 40')
elif imc > 41:
    print('Obesidade Mórbida, imc > 41')