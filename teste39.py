# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai 
# se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
print('Bem vindo ao serviço militar obrigatorio')
atual = datetime.datetime.now()
nascimento = int(input('Qual sua data de nascimento:'))
idade = atual.year - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento,idade,atual))
if idade > 18:
    saldo = 18 - idade
    print('Você tem que se alistar rapido, e esta atrasado: {} anos'.format(saldo))
elif idade == 18:
    print('Esta na hora de se apresentar agora')
elif idade < 18:
    saldo = idade - 18
    print('Voce ainda nao precisa se alistar até {} ano'.format(saldo))