jogador = {
    'nome':str(input('Informe o nome do jogador: ')).capitalize().strip()
}
gols = []
tot = 0
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(jogos):
    g = int(input(f'Quantos gols {jogador["nome"]} fez no {c+1}º jogo? '))
    gols.append(g)
    tot += g
jogador['gols'] = gols
jogador['total'] = tot
print(jogador)
print('-=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=-' * 30)
print(f'O jogador {jogador["nome"]} fez {jogos} partidas.')
for c in range(len(gols)):
    print(f'    => Na partida {c+1}, fez {gols[c]}')

