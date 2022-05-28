s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1
print('O somatório de números ímpares, múltiplos de 3 entre 1 e 500 é igual a \033[7;32m{}\033[m, e existem {} números'.format(s, cont))