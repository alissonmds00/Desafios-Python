n = int(input('Digite um número: '))
soma = maior = menor = n
c = 1
m = soma/c
mais = 'SIM'
while 'S' in mais[0]:
    mais = str(input('Deseja adicionar mais algum número? [S/N] ')).strip().upper()
    if 'S' in mais[0]:
        c += 1
        n = int(input('Digite mais um número: '))
        soma += n
        média = soma/c
        if c > 1:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
print('Você digitou {} números. A média entre eles é {:.2f}'.format(c, média))
print('{} é o menor e {} o maior'.format(menor, maior))
