import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
r = random.sample([n1, n2, n3, n4], k=4, counts=None)
#o random.sample serve para criar uma lista sem repetições
#Já o random.choice serve para escolher um único elemento
#Não esquecer de colocar os colchetes para incluir os objetos!
print('A ordem de apresentação será: {}'.format(r))


