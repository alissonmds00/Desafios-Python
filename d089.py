from time import sleep
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
while True:
    for c in range(len(boletim)):
        print(f'{c} para {boletim[c][0]}')
    print('999 para parar')
    mais = int(input('Deseja visualizar as notas de qual aluno?: '))
    if mais != 999 and mais < len(boletim):
        print(f'As notas de {boletim[mais][0]} foram {boletim[mais][1]} e {boletim[mais][2]}')
        sleep(3)
    elif mais != 999 and mais >= len(boletim):
        mais = int(input(f'Aluno não encontrado. Deseja visualizar as notas de qual aluno?: valores entre [{0}] e [{len(boletim)-1}] '))
    else:
        break



