jogador = {}
jogadores = []
mais = ''
gt = 0
while True:
    gol = []
    jogador['nome'] = str(input('Informe o nome do jogador: ')).strip().capitalize()
    jogos = int(input(f'Digite quantos jogos {jogador["nome"]} jogou: '))
    for c in range(jogos):
        g = int(input(f'Quantos gols {jogador["nome"]} fez no {c+1}º jogo? '))
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
    if mais[0] == 'N':
        break
print(jogadores)


