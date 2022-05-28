from random import randint
from time import sleep
print('-*-' * 10)
print('\033[36mAnalisando...\033[m')
print('-*-' * 10)
lista = []
r = s = 0
for c in range(1, 6):
    a = randint(0, 1)
    if a == 0:
        r += 1
    else:
        s += 1
    lista.append(a)
sleep(3)
print(f' Os números sorteados foram: {lista}')
sleep(1.5)
print('-=-' * 10)
print('RESULTADO')
if r >= 3:
    print(f'Vocês vão jogar \033[1;31mRainbow\033[m')
if s >= 3:
    print(f'Vocês vão assistir \033[1;31mSteven\033[m')
print('-=-' * 10)


