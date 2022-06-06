jogador = {}
jogadores = []
mais = ''
gt = 0
cont = 0
while True:
    gol = []
    jogador['nome'] = str(input('Informe o nome do jogador: ')).strip().capitalize()
    jogos = int(input(f'Digite quantos jogos {jogador["nome"]} jogou: '))
    for c in range(jogos):
        g = int(input(f'    Quantos gols {jogador["nome"]} fez no {c+1}º jogo? '))
        gt += g
        gol.append(g)
    jogador['gols'] = gol
    jogador['total'] = gt
    jogadores.append(jogador.copy())
    jogador.clear()
    mais = input('Deseja adicionar mais algum jogador? [S/N]: ').strip().upper()
    gt = 0
    while mais[0] not in 'SN':
        print('\033[31mDigite [s] para adiiconar mais um jogador ou [n] para parar:\033[m ')
        mais = input('Deseja adicionar mais algum jogador? [S/N]: ').strip().upper()
    c += 1
    if mais[0] == 'N':
        break
print('-=-' * 30)
print('dados || nome                Gols                Total')
print('-=-' * 30)
for c in range(len(jogadores)):
    print(f'{c} {str(jogadores[c]["nome"]):<10}    {str(jogadores[c]["gols"]):^20}    {str(jogadores[c]["total"]):^3}')
dados = 0
while dados != 999:
    dados = int(input(f'Deseja ver detalhadamente as estatisticas de qual jogador? [999] para parar, ou valores entre [0] e [{len(jogadores)}] para visualizar os jogadores: '))
    if dados == 999:
        break
    print('===' * 30)
    while dados >= len(jogadores):
        dados = int(input(f'Deseja ver detalhadamente as estatisticas de qual jogador? [999] para parar, ou valores entre [0] e [{len(jogadores)}] para visualizar os jogadores: '))        
    print(f'Levantamento do jogador {jogadores[dados]["nome"]}:')
    for c, v in enumerate(jogadores[dados]["gols"]):
        print(f'No jogo {c+1} o jogador fez {v}')
    print('==='* 30)
