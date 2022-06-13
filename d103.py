def jogador(nome='', g=0):
    """
    A função jogador() recebe como parâmetros:
    nome e g. Caso nome esteja vazio, o jogador será admitido com nome "desconhecido"
    O mesmo vale para a quantidade de gols.
    Para ter uma visualizar a saída, é necessário usar o print(jogador())
    """
    nome = str(input('Digite o nome do jogador: ')).strip()
    if nome == '':
        nome = '<desconhecido>'
    g = str(input(f'Informe a quantidade de gols de {nome}: '))
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    return f'O jogador {nome} fez {g} gols.'

print(jogador())
#print(help(jogador))