print('-*-' * 20)
n = int(input('Digite o número o qual você deseja exibir a tabuada: '))
print('-*-' * 20)
c = 0
print(f'\033[36mTabuada de {n}:\033[m')
if n >= 0:
    while c < 10:
        c += 1
        print(f'{n} x {c} = {n * c} ')
        if c == 10:
            print('-*-' * 20)
            n = int(input('Digite a nova tabuada que deseja exibir: '))
            print(f'\033[36mTabuada de {n}:\033[m')
            c = 1
            c += 1
        if n < 0:
            break
print('\033[36mTabuada finalizada.\033[m')


