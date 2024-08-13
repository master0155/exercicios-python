# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
numero=(input('Print estou pensando em um numero de 0 a 5, sabe qual é? '))
#print('acertou' if numero==5 else 'acertou')
while numero != '5':
    numero=(input('errou tente novamente: '))
print('Fim do jogo')
