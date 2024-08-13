# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
mulheres = list()
acima = list()
count = 0
count1 = 0
soma = 0
while True:
    nome = str(input('Nome:'))
    sexo = str(input('Sexo:[M/F]'))
    if sexo == 'F':
        count1 += 1
        mulheres.append(nome)
    idade = int(input('Idade:'))
    soma += idade
    count += 1
    media = soma / count
    if idade > media:
        acima.append(nome)
    if sexo != 'M' and sexo != 'F':
        print('Digite apenas M ou F, para masculino e feminino.')
        sexo = str(input('Sexo:[M/F]'))
    continuar = str(input('Deseja continuar? (não ou sim) '))
    if continuar != 'sim' and continuar != 'não':
        print('Responda apenas com sim ou não')
        continuar = str(input('Deseja continuar? (não ou sim) '))
    if continuar == 'não':
        break
print(f'Ao todo temos {count} pessoas cadastradas')
print(f'A media de idade é igual a {media:.1f} anos')
print(f'As mulheres cadastradas foram {mulheres}')
print(f'Lista das pessoas que estão acima da media de idade: {acima}')
# Feito sem uso de dicionario como variavel composta.
#clear()
#cop()