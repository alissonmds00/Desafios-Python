from time import sleep
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
e = int(input('''Dadas as opções abaixo, escoolha qual deseja:
[1] - Somar
[2] - Multiplicar
[3] - Maior e menor
[4] - Trocar os números
[5] - Sair
\033[34mO que deseja fazer?\033[m '''))
while e != 5:
    if e == 1:
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    if e == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, n1*n2))
    if e == 3:
        if n1 == n2:
            print('Entre {} e {}, não há número maior pois são iguais.'.format(n1, n2))
        if n1 > n2:
            print('Entre {} e {}, o número maior é {}.'.format(n1, n2, n1))
        if n2 > n1:
            print('Entre {} e {}, o número maior é {}.'.format(n1, n2, n2))
    if e == 4:
        n1 = float(input('Digite o novo primeiro número: '))
        n2 = float(input('Digite o novo segundo número: '))
    if e > 5 or e <= 0:
        print('\033[31mVocê digitou uma opção inválida. Tente novamente.\033[m')
    sleep(1.5)
    e = int(input('''Dadas as opções abaixo, escoolha qual deseja:
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior e menor
    [4] - Trocar os números
    [5] - Sair
    \033[34mO que deseja fazer?\033[m '''))
print('\033[32mPrograma finalizado\033[m')



