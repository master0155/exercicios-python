#  Escreva um programa que pergunte a quantidade de Km percorridos
#  por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#  Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('quantos dias alugados? '))
km = float(input('quantos km você andou com ele? '))
preco1 = int(dias * 60)
preco2 = float(km * 0.15)
total = preco1+preco2
print(f'O total a pagar é {total}')
