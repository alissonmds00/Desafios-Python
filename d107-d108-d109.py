import moedas

v = int(input('Qual o valor deseja que seja feita essa alteração? '))
a = int(input('Em quantos por cento deseja AUMENTAR o valor? '))
d = int(input('Em quantos por cento deseja DIMINUIR o valor? '))
moedas.moeda()
print(f'Ao aumentar {a}%, o resultado final é {moedas.moeda(moedas.aumentar(a, v))}')
print(f'Ao diminuir {d}%, o resultado final é {moedas.moeda(moedas.reduzir(d, v))}')
print(f'O dobro de {moedas.moeda(v)} é {moedas.moeda(moedas.dobro(v))}')
print(f'A metade de {moedas.moeda(v)} é {moedas.moeda(moedas.metade(v))}')

