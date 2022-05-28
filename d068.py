from random import randint
from time import sleep
print('-*-' * 20)
print('\033[36mPar\033[m ou \033[34mImpar\033[m')
print('-*-' * 20)
sleep(1)
esc = int(input('Escolha um número: '))
pi = str(input('Escolha entre par ou impar [P/I] ')).strip().upper()
pc = randint(0, 10)
c = 0
p = 0
r = esc + pc
while pi[0] != 'P' and pi[0] != 'I':
    esc = int(input('Escolha um número: '))
    pi = str(input('Escolha entre par ou impar [P/I] ')).strip().upper()
    pc = randint(0, 10)
    print('-*-' * 20)
if r%2 == 0 and pi[0] == 'P':
    print(f'Sua escolha foi PAR. O seu número foi {esc} e a do computador: {pc}. Você venceu!')
    c += 1
    p = c
elif r%2 != 0 and pi[0] == 'I':
    print(f'sua escolha foi IMPAR. O seu número foi {esc} e a do computador: {pc}. Você venceu!')
    c += 1
    p = c
while p > 0:
    print('-*-' * 20)
    esc = int(input('Escolha um número: '))
    pi = str(input('Escolha entre par ou impar [P/I] ')).strip().upper()
    pc = randint(0, 10)
    r = esc + pc
    if r%2 == 0 and pi[0] == 'P':
        print(f'Sua escolha foi PAR. O seu número foi {esc} e o do computador {pc}. Você venceu!')
        c += 1
        p = c
    if r%2 != 0 and pi[0] == 'I':
        print(f'Sua escolha foi IMPAR. O seu número foi {esc} e o do computador {pc}. Você venceu!')
        c += 1
        p = c
    if r%2 == 0 and pi[0] == 'I':
        p = c
        c == 0
        break
    if r%2 != 0 and pi[0] == 'P':
        p = c
        c == 0
        break
if r%2 == 0 and pi[0] == 'I':
    print(f'Sua escolha foi IMPAR. O seu número foi {esc} e a do computador {pc}. Você perdeu.')
    print(f'Você  venceu o computador {p} vezes.')
    p = c
    c == 0
if r%2 != 0 and pi[0] == 'P':
    print(f'sua escolha foi PAR. O seu número foi {esc} e o do computador {pc}. Você perdeu.')
    print(f'Você venceu o computador {p} vezes.')
    p = c
    c == 0


