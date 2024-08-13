# Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def linha():
    print('='*17)
def idade(a=0,b=0):
    a = int(input('Qual a sua idade?'))
    b = 18
    if a > b:
        print(f'Com idade {a} o voto é obrigatorio no Brasil.')
    if a < b:
        print(f'Com idade {a} o voto é opcional para menores de idade.')


linha()
idade()
linha()