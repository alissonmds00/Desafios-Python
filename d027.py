#faça um programa que leia o nome completo de uma pessoa. mostrando em seguida o primeiro e o último nome
#SEPARADAMENTE
nome = str(input('Digite o seu nome completo: ')).strip().title().split()
print('Olá, {} {}'.format(nome[0], nome[-1]))








