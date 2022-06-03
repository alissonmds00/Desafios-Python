matriz = [[], [], []]
cont = 0
n = 0
for c in range(9):
    if c < 3:
        n = int(input(f'Digite o número que será colocado na posição [1], [{c+1}]: '))
        matriz[0].append(n)
    elif 5 >= c >= 3:
        n = int(input(f'Digite o número que será colocado na posição [2], [{c-2}]: '))
        matriz[1].append(n)
    else:
        n = int(input(f'Digite o número que será colocado na posição [3], [{c-5}]: '))
        matriz[2].append(n) 
print('-*-' * 30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('-*-' * 30) 