camp = ('', 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo', 'Internacional', 'Corinthians',
        'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa',
        'Chapecoense', 'Avaí')
print('-*-' * 100)
print(f'Os times são: {camp[1::]}')
print('-*-' * 100)
print(f'Estes são os 5 primeiros colocados: \033[33m{camp[1:6]}\033[m')
print('-*-' * 100)
print(f'Estes são os 4 últimos colocados: \033[31m{camp[17:]}\033[m')
print('-*-' * 100)
print(f'Os times em ordem alfabética {sorted(camp)}')
print('-*-' * 100)
print(f'A Chapecoense está na \033[32m{camp.index("Chapecoense")}ª\033[m posição')
