s = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor '.format(c)))
    if n % 2 == 0:
        s = n + s
print('Dentre os números digitados, a soma dos pares é: {}'.format(s))
