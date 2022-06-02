lista = []
for c in range(0, 5):
    n = int(input(f'Digite o número da posição {c}: '))
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
for c, v in enumerate(lista):
    if c < len(lista)-1:
        print(v, end=" ")
    else:
        print(v)





