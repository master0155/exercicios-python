# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ('bola', 'magia', 'cortina', 'livro')
for c in tupla:
    print(f'\n Na palavra {c} temos: ', end = '')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end = '')