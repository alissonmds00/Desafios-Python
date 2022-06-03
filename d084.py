lista = []
cadastros = []
mai = men = 0
mais = " "
while True:
    if mais[0] == "N":
        break
    lista.append(input("Digite o nome: ").strip())
    lista.append(input("Digite o peso: "))
    if len(cadastros) == 0:
        mai = men = lista[1]
    if lista[1] < men:
        men = lista[1]
    if lista[1] > mai:
        mai = lista[1]
    cadastros.append(lista[:])
    lista.clear()
    mais = str(input("Deseja adicionar mais pessoas? [S/N]: ")).strip().upper()
    while mais[0] not in "SN":
        mais = str(input("Deseja adicionar mais pessoas? [S/N]: ")).strip().upper()
print(f'Ao todo foram cadastradas {len(cadastros)} pessoas')
print(f'O maior peso foi de {mai}Kg e foi de:', end=" ")
for p in cadastros:
    if p[1] == mai:
        print(f"\033[1;32m{p[0]}\033[m", end=' ')
print()
print(f'O menor peso foi de {men}Kg e foi de:', end=" ")
for p in cadastros:
    if p[1] == men:
        print(f"\033[1;33m{p[0]}\033[m", end=" ")
