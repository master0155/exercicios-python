# Escreva um programa que pergunte o salário de um funcionário, calcule
# o valor do seu aumento. Para salários superiores a R$1250,00, calcule
# um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual o salario do funcionario?'))
if salario<=1250.00:
    aumento=salario*15 / 100
    salario=salario+aumento
else:
#if salario>1250:
    aumento=salario*10/ 100
    salario+=aumento
print('Seu novo salario com aumento fica: {}'.format(salario))
