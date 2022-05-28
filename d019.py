import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
r = random.choice([n1, n2, n3, n4])
print('O aluno escolhido foi: \033[1;34m{}\033[m! '.format(r))
#poderia ser feita uma lista, usando colchetes
#lista = [n1, n2, n3, n4]
# e colocada dentro de random.choice(lista)