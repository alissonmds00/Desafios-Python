matriz = [[], [], []]
pares = 0
coluna3 = 0
for linha in range(3):
    for coluna in range(3):
        n = int(input(f'Digite o valor que será inserido em [{linha+1}], [{coluna+1}]: '))
        matriz[linha].append(n)
        if n % 2 == 0:
            pares += n
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
        if coluna == 2:
            coluna3 += matriz[linha][2]
    print()
maior = max(matriz[1])
print('-=-' * 30)
print(f'A soma dos valores pares é igual a {pares}')
print(f'A soma dos valores da terceira coluna é: \033[31m{coluna3}\033[m')
print(f'O maior valor da linha 2 é: \033[36m{maior}\033[m')
 