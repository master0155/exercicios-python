# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(txt):
    tam = len(txt)
    print('=' * tam)
    print(txt)
    print('=' * tam)
   

oi = escreva('Era uma vez')