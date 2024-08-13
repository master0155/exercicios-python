# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.
produto=float(input('Qual preço do nosso produto? R$'))
print('achou caro? te faço um desconto')
print('temos um super desconto de 5%')
desconto=(produto * 5 / 100)
novo = produto - desconto
print('O preco do produto com desconto é {}'.format(novo))
print('Volte sempre.')
# (* 5 / 100) (achar a porcentagem)
