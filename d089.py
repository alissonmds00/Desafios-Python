mais = ''
boletim = []
notas = []
resultado = []
media = 0
while True:
    nome = str(input('Informe o nome d@ alun@: '))
    notas.append(nome)
    nota1 = float(input('Informe a primeira nota: '))
    notas.append(nota1)
    nota2 = float(input('Informe a segunda nota: '))
    notas.append(nota2)
    boletim.append(notas[:])
    notas.clear()
    mais = str(input('Deseja adicionar mais algum aluno? [S/N] ')).strip().upper()
    while mais[0] not in "SN":
        mais = str(input('Deseja adicionar mais algum aluno? [S/N] ')).strip().upper()
    if mais[0] == "N":
        break
for quant in range(len(boletim)):
    for notas in range(1, 3):
        media += boletim[quant][notas]
    resultado.append(media/2)
    media = 0
for c in range(len(boletim)):
    print(f'A média de {boletim[c][0]}, foi {resultado[c]}')
print(f'Para qual aluno deseja visualizar as notas? [999 para parar] ', end=" ")
for c in range(len(boletim)):
    print(f'{c} para {boletim[c][0]}')
"""while True:
    if mais == 999:
        break
    while mais != 999:
        num = int(input(f'Digite o número do aluno que deseja ver as notas: '))
        print(f'As notas de {')"""
