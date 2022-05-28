produtos = ('Pão', 1.50, 'Leite', 20.00, 'Açúcar', 5.00, 'Sal', 1.00, 'Manteiga', 15.00, 'Café', 7.00, 'Pastel', 6.00)
ponto = 0
print('-' * 40)
print(f'{" " * 12}\033[1m{"LISTA DE PREÇOS"}\033[m')
print('-' * 40)
for c in range(0, len(produtos), 2):
    ponto = (20 - len(produtos[c]))
    print(f'{produtos[c]} {"." * ponto} R$: {produtos[c+1]:.2f}')
print('-' * 40)

