# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros
compra = float(input('Preço das compra:'))
print('opção 1, à vista dinheiro/cheque')
print('opção 2, à vista no cartão')
print('opção 3, em até 2x no cartão')
print('opção 4, 3x ou mais no cartão')
escolha = int(input(' escolha uma das formas de pagamento:'))
if escolha == 1:
    opcao1 = compra - compra * 0.10
    print('Vai custar:', opcao1)
elif escolha == 2:
    opcao2 = compra - compra * 0.05
    print('Vai custar:', opcao2)
elif escolha == 3:
    opcao3 = compra 
    print('Vai custar:', opcao3)
elif escolha == 4:
    opcao4 = compra + compra * 0.20
    print('Vai custar:', opcao4)
else:
    print('Desistencia da compra confirmada.')
    