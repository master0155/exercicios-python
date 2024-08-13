# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
def area(larg , comp):
    s = (larg * comp) / 2
    print(f'A area de um terreno com a largura {larg} e o comprimento {comp} é {s}m²')


print('Controle de terreno')
largura = float(input('Qual a largura da sua parede?'))
comprimento = float(input('Qual o comprimento da sua parede?'))
area(larg=largura,comp=comprimento)