num = []
pos = 0
maior = menor = 0
posM = []
posm = []
for cont in range(0, 5):
    n = int(input(f'Digite o número da posição {cont}: '))
    num.append(n)
    if cont == 0:
        maior = n
        menor = n
    else:
        if maior > n:
            maior = n
        if menor < n:
            menor = n
for c, pos in enumerate(num):
    if pos == maior:
        posM.append(c)
    if pos == menor:
        posm.append(c)
print(f'Os números digitados foram {num}')
print(f'O maior número é {maior} nas posições {posM}', end= '')
print(f'\nO menor número é {menor} nas posições {posm}', end= '')
num.sort()
print(f'Os números em ordem crescente: {num}')




