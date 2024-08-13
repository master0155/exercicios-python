# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
# em ordem, sabendo que o vencedor tirou o maior número no dado.
import random
dicionario = {
    'jogador1': random.randint(1,5),
    'jogador2': random.randint(1,5),
    'jogador3': random.randint(1,5),
    'jogador4': random.randint(1,5)
}
for c in sorted(dicionario,key=dicionario.get, reverse=True) :    
    print(c,dicionario[c])
    