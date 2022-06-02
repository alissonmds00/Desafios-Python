from pstats import SortKey
lista = []
cadastros = []
mais = " "
maisp = []
maisl = []
while True:
    if mais[0] == "N":
        break
    nome = str(input("Digite o nome: "))
    lista.append(nome)
    peso = int(input("Informe o peso: "))
    lista.append(peso)
    cadastros.append(lista[:])
    mais = str(input("Deseja adicionar mais pessoas? [S/N]: ")).strip().upper()
    while mais[0] not in "SN":
        mais = str(input("Deseja adicionar mais pessoas? [S/N]: ")).strip().upper()
quant = len(cadastros)
if quant % 2 == 0:
    pesados = leves = quant//2
else:    
    pesados = leves = ((quant//2) - 1)
cadastros.sort(key=itemgetter(1))
for cont, pesos in enumerate(cadastros): # pesos aqui é usado para os valores dos pesos
    if cont <= pesados:
        maisp.append(pesos)
        maisl.append(pesos)
    else:
        for d in range(pesados):
            if pesos[cont][1] > maisp[d][1]:
                maisp.append()
print(f'Foram cadastradas {quant} pessoas.')


    