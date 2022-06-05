from math import trunc
pessoa = {}
mais = ''
cont = 0
cadastros = []
mulheres = []
velhos = []
while True:
    n = str(input(f'Informe o nome da {cont+1}ª pessoa: ')).strip().capitalize()
    pessoa['nome'] = n
    s = str(input(f'Informe o sexo da {cont+1}ª pessoa [M/F]: ')).upper().strip()
    while s[0] not in 'MF':
        print('\033[31mSexo inválido.\033[m')
        s = str(input(f'Informe o sexo da {cont+1} pessoa [M/F]: ')).upper().strip()
    pessoa['sexo'] = s
    i = int(input(f'Informe a idade da {cont+1}ª pessoa '))
    pessoa['idade'] = i
    mais = str(input('Deseja cadastrar mais alguma pessoa? [S/N]: ')).strip().upper()
    while mais[0] not in 'SN':
        print('\033[31mOpção inválida\033[m')
        mais = str(input('Deseja cadastrar mais alguma pessoa? [S/N]: ')).strip().upper()
    cont += 1
    cadastros.append(pessoa.copy())
    if mais[0] == 'N':
        break
print(f'Foram cadastradas {len(cadastros)} pessoas no total')
im = 0
for c in range(len(cadastros)):
    im += (cadastros[c]['idade'])
    if cadastros[c]['sexo'] == "F":
        mulheres.append(cadastros[c]['nome'])
im = im/len(cadastros)
im = trunc(im)
print(f'A média das idades é igual a {im} anos')
print('As mulheres cadastradas são:', end=' ')
for c in range(len(mulheres)):
    print(mulheres[c], end=' ')
print()
print(f'As pessoas acima da idade média que é {im} são:', end=' ')
for c in range(len(cadastros)):
    if cadastros[c]['idade'] > im:
        velhos.append(cadastros[c]['nome'])
for c in range(len(velhos)):
    print(velhos[c], end=' ')

    



 





