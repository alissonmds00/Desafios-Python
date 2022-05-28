mais = ''
num = []
n = int(input('Digite um número: '))
print('Valor adicionado!')
num.append(n)
c = 1
while mais != 'N' or mais != 'S':
    mais = str(input('Deseja adicionar mais números? [S/N] ')[0]).upper().strip()
    while mais == 'S':
        n = int(input('Digite outro número: '))
        c += 1
        if n not in num:
            num.append(n)
            print('Valor adicionado!')
        else:
            print('Valor duplicado. Não será adicionado')
        mais = str(input('Deseja adicionar mais números? [S/N] ')[0]).upper().strip()
    if mais == 'N':
        break
num.sort()
print(f'Foram digitados {c} números;')
print(f'A lista é composta por {num};')
print(f'Foram digitados {c-len(num)} números repitidos.')
num.sort(reverse=True)
print(f'A lista é composta por {num} ')

