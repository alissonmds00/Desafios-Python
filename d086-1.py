lista = [[], [], []]
for linha in range(3):
    for coluna in range(3):
        n = int(input(f'Digite o número que será armazenado em [{linha}], [{coluna}]: '))
        lista[linha].append(n)
"""for matriz in range(3):
    print(f'{lista[matriz]}')""" # Aqui já funciona, mas um jeito para contornar os números de tamanhos diferentes é:
for l in range(3):
    for c in range(3):
        print(f'[{lista[l][c]:^5}]', end=' ') # alinha tudo no centro por conta do ':^5'
    print()
