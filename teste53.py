# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
frase = input('Digite uma palavra:')
print('Se for um palindromo a palavra sera exibida novamente')
if frase[::-1] == frase:
    print(frase[::-1])
else:
    print('Não é um palindromo.')