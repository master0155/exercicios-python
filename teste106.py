# Faça um mini-sistema que utilize
# o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
def ajuda(txt):
    help(txt)


comando = ''
while True:
    comando = str(input('Digite o comando ou biblioteca para ver suas instruções:'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
