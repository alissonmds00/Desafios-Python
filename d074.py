from random import randint
n = []
maior = 0
menor = 0
for c in range(1, 6):
    num = randint(1, 10)
    n.append(num)
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Os números sorteados foram: {n}')
print(f'O maior número foi {maior}\ne o  menor número foi {menor}')
