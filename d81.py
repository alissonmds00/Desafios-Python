c = 0
lista = []
while True:
    if mais[0] == "N":
        break
    n = int(input(f'Digite o {c+1}º número: '))
    lista.append(n)
    mais = str(input("Deseja adicionar mais algum número? [S/N]: ")).upper().strip()
    c += 1
    while mais[0] not in "NS":
        mais = str(input("Deseja adicionar mais algum número? [S/N]: ")).upper().strip()
        if mais[0] == "N":
            break
lista.sort(reverse=True)
print(f"Foram digitados {c} valores")
print(lista)
if 5 not in lista:
    print("O número 5 não está na lista")
else:
    print(f"O número 5 está na lista")

