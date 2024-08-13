# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoasepesotemp = []
pessoasepeso = []
contador = 0
continuar = 'S'

while continuar == 'S':
    pessoasepesotemp.append(input('digite o nome:'))
    pessoasepesotemp.append(int(input('digite um peso:')))
    
    if len(pessoasepeso) == 0:
        maior = menor = pessoasepesotemp[1]
    else:
        if pessoasepesotemp[1] >  maior:
            maior = pessoasepesotemp[1]
        elif pessoasepesotemp[1] < menor:
            menor = pessoasepesotemp[1]
    
    pessoasepeso.append(pessoasepesotemp[:])
    pessoasepesotemp.clear()

    contador += 1
     
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
print(f'foram cadastradas {contador} pessoas.')

print(f'a(s) pessoa(s) mais pesada(s) foi {maior} da(s) pessoa(s) ', end ='')
for pessoas in pessoasepeso:
    if pessoas[1] == maior:
        print(f'{pessoas[0]} ')

print(f'a(s) pessoa(s) mais leve(s) foi {menor} da(s) pessoa(s) ', end ='')
for pessoas in pessoasepeso:
    if pessoas[1] == menor:
        print(f'{pessoas[0]} ', end ='')