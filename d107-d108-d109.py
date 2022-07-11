import moedas

v = int(input('Qual o valor deseja que seja feita essa alteração? '))
a = int(input('Em quantos por cento deseja AUMENTAR o valor? '))
d = int(input('Em quantos por cento deseja DIMINUIR o valor? '))
moedas.moeda()
print(f'Ao aumentar {a}%, o resultado final é {moedas.aumentar(a, v, True)}')
print(f'Ao diminuir {d}%, o resultado final é {moedas.reduzir(d, v, True)}')
print(f'O dobro de {moedas.moeda(v)} é {moedas.dobro(v, True)}')
print(f'A metade de {moedas.moeda(v)} é {moedas.metade(v, True)}')

