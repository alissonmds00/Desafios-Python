lista = []
maior = menor = 0
pos1 = []
pos2 = []
for c in range(1, 6):
    n = int(input(f'Digite o {c}º valor: '))
    lista.append(n)
    if c == 1:
        maior = n
        menor = n
        pos1.append(c)
        pos2.append(c)
    else:
        if n > maior:
            pos1.clear()
            maior = n
            pos1.append(c)
        if n < menor:
            pos2.clear()
            menor = n
            pos2.append(c)
        if n == maior:
            pos1.append(c)
        if n == menor:
            pos2.append(c)
print(f'Os números digitados foram {lista}')
print(f'Sendo o maior deles {maior} e o menor deles {menor}')
print(f'E ocupam respectivamente a {pos1}ª e {pos2}ª posição na lista')