from random import randint
n = ((randint(1, 10)), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: {n}', end=' ')
print(f'\nO valor máximo foi {max(n)}')
print(f'O valor mínimo foi {min(n)}')