# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
lista = list()
dicionario = dict()
while True:
    nome = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    gols = list()
    lista.append([nome, [gols], partidas])
    soma = 0
    for c in range(1,partidas+1):
        jogos1 = int(input(f'Quantos gols na partida {c}?: '))
        soma += jogos1 
        gols.append(jogos1)
    continuar = str(input('Deseja continuar sim ou não?'))
    if continuar == 'não':
        break
dicionario["nome"] = nome
dicionario["gols"] = gols
dicionario["soma"]= soma
print(lista)
print(f'O campo nome têm o valor {dicionario["nome"]}')
print(f'O campo gols têm o valor {dicionario["gols"]}')
print(f'O campo total de gols têm o valor {dicionario["soma"]}')
for partidas in range(0,len(gols)):
    print(f'Na partida {partidas} fez {gols[partidas]} gols')
while True:
    busca = (input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == '999':
        break
    if busca >= len(lista):
        print(f'Não existe esse jogador com código {busca}')
    else:
        print(f'Levantamento do jogador (nome):{dicionario[busca]["nome"]}')
        print(f'Levantamento do jogador (gols):{lista[busca]["gols"]}')
        print(f'Levantamento do jogador (total de gols):{lista[busca]["soma"]}')
