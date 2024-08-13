# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
from time import sleep
n1 = int(input('Escolha um numero para ser exibida sua tabuada do 1 ao 10: '))
for c in range(1, 11): 
    print('{}x{}={}'.format(n1, c, c *n1))
    sleep(0.5)