from random import randint
from time import sleep
def sortear(lista):
    print(f'Os números sorteados são: ', end='')
    for c in range(5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print()

def somapar(lista):
    par = 0
    for v in lista:
        if v % 2 == 0:
            par += v
    print(f'Somando os valores pares de {lista}, temos {par}')


num = []
sortear(num)
somapar(num)