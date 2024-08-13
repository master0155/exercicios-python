# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
pessoa = dict()
nome = str(input('Nome: '))
idade = int(input('Idade: '))
trabalho = str(input('Carteira de trabalho (0 não tem): '))
pessoa["nome"] = nome
pessoa["idade"] = idade
pessoa["trabalho"] = trabalho
if trabalho != '0':    
    contrato = int(input('Ano de contratação: '))
    salario = float(input('Salario: '))
    pessoa["contrato"] = contrato
    pessoa["salario"] = salario
    aposentadoria = contrato+35-2022+idade
    pessoa["aposentadoria"] = aposentadoria
print('-~'*25)
print(f'Nome é igual a: {pessoa["nome"]}')
print(f'Idade é igual a: {pessoa["idade"]}')
print(f'Numero da carteira de trabalho é igual: {pessoa["trabalho"]}')
print(f'Ano de contrato é igual a: {pessoa["contrato"]}')
print(f'Salario é igual a: R${pessoa["salario"]}')
print(f'Aposentadoria é igual a {pessoa["aposentadoria"]} anos de idade.')    
