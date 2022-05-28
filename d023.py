n = int(input('Digite o número desejado entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('''A unidade é {}
A dezena é {}
A centena é {}
A unidade de milhar é {}.'''.format(u, d, c, m))


