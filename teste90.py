# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.
dicionario = dict()
nome = str(input('Digite o seu nome: '))
media = float(input('Digite a sua média: '))
dicionario['nome'] = nome
dicionario['media'] = media
print(f' - Nome é igual a: {dicionario["nome"]}')
print(f' - Média é igual a: {dicionario["media"]}')
if media >= 7.0:
    dicionario["situacao"] = 'aprovado'
else:
    dicionario["situacao"] = 'reprovado'
print(f' - Situação é igual a: {dicionario["situacao"]}')
