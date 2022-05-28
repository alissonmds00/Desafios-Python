c = n = int(input('Digite o número para calcular o seu fatorial: '))
fat = 1
print('{}! ='.format(n), end='')
for c in range(n, 0, -1):
    print(' {} '.format(c), end='')
    print('x' if c > 1 else ' = ', end='')
    fat = fat * c
    c = c - 1
print('{}'.format(fat))