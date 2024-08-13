# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto
sexo = input('Qual o seu genero? (Apenas M ou F)')
while not sexo == 'M' and not sexo =='F':
    sexo = input('Qual o seu genero? (Apenas M ou F)')
print('fim')
