from time import sleep
from random import randint
n = int(input('Digite a quantidade de jogos que você deseja que sejam gerados: '))
print('-=-' * 30)
print(f'Gerando {n} listas...')
print('-=-' * 30)
sleep(1)
lista = []
valores = []
for linha in range(n):
    for coluna in range(6):
        n = randint(1, 60)
        valores.append(n)
    lista.append(valores[:])
    valores.clear()
for l in range(len(lista)):
    print(f'Lista número {l+1}: ', end=' ')
    for c in range(6):
        print(f'[{lista[l][c]:^5}]', end=' ')
    sleep(1)
    print()
