n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont = cont + 1
        print('\033[32m', end='')
    else:
        c = c + 0
        print('\033[m', end='')
    print('{} '.format(c), end='')
if cont == 2:
    print('\n\033[m{} é um número primo, pois só é divisível por: {} e {}'.format(n, '1', n))
elif cont == 1:
    print('\n\033[m1 não é um número primo.')
else:
    print('\n\033[m{} não é um número primo, pois foi divisível {} vezes'.format(n, cont))
