# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dicionario = dict()
nome = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {nome} jogou? '))
gols = list()
soma = 0
for c in range(1,partidas+1):
    jogos1 = int(input(f'Quantos gols na partida {c}?: '))
    soma += jogos1 
    gols.append(jogos1)
dicionario["nome"] = nome
dicionario["gols"] = gols
dicionario["soma"]= soma
print('/' *35)
print('dados:',dicionario)
print(f'O campo nome têm o valor {dicionario["nome"]}')
print(f'O campo gols têm o valor {dicionario["gols"]}')
print(f'O campo total de gols têm o valor {dicionario["soma"]}')
print('/' *35)
for partidas in range(0,len(gols)):
    print(f'Na partida {partidas} fez {gols[partidas]} gols')