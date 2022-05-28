print('||=====================================================||')
print('\033[35mSequência de Fibonacci\033[m')
print('||=====================================================||')
n = int(input('Digite a quantidade de números que deseja exibir: '))
t1 = 0
t2 = 1
print('{} ➙ {}'.format(t1, t2), end=' ➙ ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('{}'.format(t3), end=' ➙ ')
    t1 = t2 #esse jogo fará com que t1 receba o valor de t2 e t2 o de t3, fazendo com q n seja necessário a criação de várias variáveis
    t2 = t3 #troca
    cont += 1
print('FIM', end='')

