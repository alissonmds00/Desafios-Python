from random import randint
from time import sleep
c = 1
print('----- Jogo da Advinhação -----')
sleep(1)
print('''Será pensado um número entre 1 e 10.
Tente advinhá-lo se puder.''')
sleep(1)
print('       QUE COMECEM OS JOGOS!')
print('-=-' * 20)
pc = randint(1, 10)
escolha = int(input('Advinha o número escolhido pelo computador: '))
while escolha != pc:
    print('Escolha errada. Tome mais uma chance!')
    c += 1
    escolha = int(input('Advinhe o número escolhido pelo computador: '))
print('Uau! Você acertou na {}ª tentativa!'.format(c))