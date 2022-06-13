cores = (
    '\033[m',
    '\033[41m',
    '\033[42m',
    '\033[43m',
    '\033[44m',
    '\033[45m',
    '\033[7;30m'
)

def ajuda(com):
    título(f'Acessando o manual do comando {com}', 4)
    print(cores[6], end=' ')
    help(com)
    print(cores[0], end=' ')


def título(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end=' ')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end=' ')    

while True:
    título('Sistema de ajuda PyHELP', 2)
    comando = str(input('Informe a Função ou Biblioteca que deseja obter ajuda > ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
    

