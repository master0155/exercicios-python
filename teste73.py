# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio','Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza','Goiás','Bahia'
,'Vasco','Atlético-MG','Fluminense','Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avaí')
print(times[0:5])
print(times[-4:])
print(sorted(times))
print(times.index('Chapecoense')+1) 