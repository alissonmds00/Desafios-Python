print('-*-' * 20)
print('\033[36mProgressão Aritimética\033[m')
print('-*-' * 20)
t = t1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
cont = 1
total = 0
mais = 10
print('{} → '.format(t1), end='')
while mais != 0:
    total = total + mais
    while cont <= total:
        cont = cont + 1
        t = t + r
        print('{}'.format(t), end=' → ')
    print('Pausa')
    mais = int(input('Deseja adicionar quantos mais termos? '))
print('O seu gerador de PA terminou após exibir {} termos'.format(cont))




