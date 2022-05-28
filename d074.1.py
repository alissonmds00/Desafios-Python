from random import randint
maior = 0
menor = 0
for c in range(1, 5):
    n = randint(1,  10)
    if c == 1:
        maior = n
        menor = n
        n1 = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
        if c == 2:
            n2 = n
        if c == 3:
            n3 = n
        if c == 4:
            n4 = n
numero = (n1, n2, n3, n4)
print(numero)
print(f'o maior número é: {maior}')
print(f'o menor número é: {menor}')

