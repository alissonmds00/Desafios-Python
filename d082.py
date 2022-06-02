lista = []
par = []
impar = []
mais = " "
while True:
    if mais[0] == "N":
        break
    lista.append(int(input("Digite um número:" )))
    mais = str(input("Deseja adicionar mais um número? [S/N]: ")).upper()
    while mais[0] not in "SN":
        mais = str(input("Deseja adicionar mais um número? [S/N]: ")).upper()
for c in range(len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print(f"Os valores digitados foram: {lista}")
print(f"Os valores pares são: {par}")
print(f'Os valores ímpares são: {impar}')