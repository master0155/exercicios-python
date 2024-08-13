# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.
salario=float(input('Quanto é o seu salario? R$'))
print('temos um aumento de 15% para você')
aumento=(salario * 15 / 100)
novo=salario + aumento
print('Agora o seu salario é de {} '.format(novo))
