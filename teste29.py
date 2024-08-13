# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade=int(input('Qual a velocidade do carro? '))
if velocidade>80:
    print('A velocidade do carro esta muito alta. você foi multado')
    multa = (velocidade - 80) * 7
    print('você deve pagar uma multa de {}$'.format(multa))
else:
    print('Boa viagem')
