# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
altura =int(input('Qual a altura da sua parede? (metros):'))
largura =int(input('Qual a largura da sua parede? (metros):'))
total =(altura * largura)
print('a area quadrada da parede é: {} (m²)'.format(total))
print('para pintar essa parede precisa de: {} litros de tinta'.format(total / 2))
