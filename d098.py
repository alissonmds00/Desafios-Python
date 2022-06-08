def contador():
    from math import fabs as mod
    from time import sleep
    i = int(input('Informe qual será o ponto de partida de contagem: '))
    f = int(input('Informe qual será o ponto final da contagem: '))
    p = int(input('Informe o intervalo entre os números de contagem: '))
    if p == 0:
        p = 1
    print('-=-' * f)
    for c in range(1, 11):
        print(f'{c}', end=' ➯ ')
        sleep(0.1)
    print('fim')
    for d in range(10, -1, -2):
        print(f'{d}', end=' ➯ ')
        sleep(0.1)
    print('fim')
    if i > f:
        for cont in range(i, f-1, -int(mod(p))):
            print(f'{cont}', end=' ➯ ')
            sleep(0.1)
    print('fim')
    if i < f:
        for cont in range(i, f+1, p):
            print(f'{cont}', end=' ➯ ')
            sleep(0.25)
    print('fim')
    print('-=-' * f)

contador()