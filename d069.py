from time import sleep
c = 0
maior = 0
homem = 0
mulher = 0
while True:
    n = int(input(f'Digite a idade da {c+1}ª pessoa: '))
    while n < 0:
        n = int(input('Repita a idade informada: '))
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Repita o sexo [M/F]: ')).strip().upper()[0]
    mais = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    while mais not in 'SN':
        mais = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('-*-' * 20)
    c += 1
    if n > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and n < 20:
        mulher += 1
    if mais == 'N':
        break
print('Analisando...')
sleep(1)
print(f'{c} pessoas foram cadastradas')
print(f'Foram cadastradas {maior} pessoas maiores de idade')
print(f'Foram cadastrados {homem} homens')
print(f'Foram cadastradas {mulher} mulheres menor de 20 anos')
print('-*-' * 20)



