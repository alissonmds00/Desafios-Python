c = 1
num = []
pares = []
for c in range(1, 5):
    n = int(input(f'Digite o {c}º número: '))
    num.append(n)
    if n % 2 == 0:
        pares.append(n)
print(f'O número 9 apareceu \033[32m{num.count(9)}\033[m vezes')

if 3 in num:
    print(f'O número 3 foi digitado a primeira vez no seu \033[34m{num.index(3) + 1}\33[mº valor digitado')  # localiza o valor
else:
    print('O número 3 não foi digitado em momento algum')
if len(pares) > 0:
    print(f'Os números pares são: {pares}')
else:
    print('Não foram digitados valores pares')

