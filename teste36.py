# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salario mensal em R$: '))
pagar = int(input('Em quantos anos voce vai pagar: '))
meses = casa / (pagar * 12)
if meses<=salario * 0.3:
    print('Você pode pagar')
else:
    print('Você não pode pagar') 
