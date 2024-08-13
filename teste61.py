# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Termo da PA: '))
termo = primeiro
count = 1
while count <= 10:
    print('{} - ', end = '')
    count +=1
print('Fim')
