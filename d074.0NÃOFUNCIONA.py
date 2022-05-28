from random import randint
cont = 1
a = b = c = d = e = maior = menor = 0
num = a, b, c, d, e,
for cont in range(1, 6):
    n = randint(1, 10)
    if cont == 1:
        maior = n
        menor = n
        a = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        if cont == 2:
            b = n
        if cont == 3:
            c = n
        if cont == 4:
            d = n
        if cont == 5:
            e = n
print(num[0:6])
print(maior)
print(menor)