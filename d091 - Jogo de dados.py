from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1':randint(1, 6), 
        'jogador 2':randint(1, 6), 
        'jogador 3':randint(1, 6), 
        'jogador 4':randint(1, 6)}
ranking = () # para fins de formatação, o ranking será tratado como lista
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'o {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=-' * 30)
print(f'{"RESULTADO":^30}')
print('-=-' * 30)
 # se o itemgetter for 1, pega os valores, se for parte 0, os nomes.
 # O reverse=True faz com que fique organizado em ordem decrescente e cumpra o papel de ranking.
for c, v in enumerate(ranking):
    print(f'{c+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)