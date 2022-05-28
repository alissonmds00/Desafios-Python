p = int(input('Digite o primeiro termo de PA: '))
r = int(input('Digite a razão da PA: '))
for c in range(1, 11):
    print('O {}º termo é igual {}'.format(c, p+(c-1)*r))
