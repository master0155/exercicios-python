# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
print('Sera que você passou de ano?')
nota = float(input('Qual a sua nota:'))
if nota<5.0: 
    print('Reprovado')
elif nota <= 6.9:
    print('Recuperação')
elif nota >= 7.0:
    print('Aprovado')