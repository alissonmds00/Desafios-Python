c = n = int(input('Digite o número que deseja calcular o fatorial: '))
fat = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print('{}'.format(fat))
