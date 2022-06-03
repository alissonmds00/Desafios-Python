matriz = [[], [], []]
pares = 0
coluna3 = 0
maior = 0
for linha in range(3):
    for coluna in range(3):
        n = int(input(f'Digite o valor que será inserido em [{linha+1}], [{coluna+1}]: '))
        matriz[linha].append(n)
        if n % 2 == 0:
            pares += n
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
        coluna3 += (matriz[linha][2])
        if coluna == 2 and linha == 0:
            maior = matriz[0][2]
        elif coluna == 2 and matriz[linha][2] > maior:
            maior = matriz[linha][2]
    print()
print('-=-' * 30)
print(f'A soma dos valores pares é igual a {pares}')
print(f'A soma dos valores da terceira coluna  {coluna3}')
print(f'O maior valor da linha 2 é {maior}')
 