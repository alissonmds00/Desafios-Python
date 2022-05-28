sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
a = ''
if 'M' in sexo:
    a = sexo.replace('M', 'masculino')
if 'F' in sexo:
    a = sexo.replace('F', 'feminino')
while sexo != 'M' and sexo != 'F':
    print('\033[31mVocê digitou um sexo inválido. Digite [M/F].\033[m')
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
    if 'M' in sexo:
       a = sexo.replace('M', 'masculino')
    if 'F' in sexo:
       a = sexo.replace('F', 'feminino')
print(f'Sexo {a} registrado com sucesso.')