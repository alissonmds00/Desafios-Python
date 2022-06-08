def contador():
    i = int(input('Informe qual será o ponto de partida de contagem: '))
    f = int(input('Informe qual será o ponto final da contagem: '))
    p = int(input('Informe o intervalo entre os números de contagem: '))
    print('-=-' * f)
    for c in range(1, 11):
        print(f'{c}', end=' ➯ ')
    print('fim')
    for d in range(10, -1, -1):
        print(f'{d}', end=' ➯ ')
    print('fim')
    for e in range(i, f+1, p):
        print(f'{e}', end=' ➯ ')
    print('fim')
    print('-=-' * f)

contador()