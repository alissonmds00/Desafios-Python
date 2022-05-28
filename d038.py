n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print('Entre {} e {}, {} é o maior.'.format(n1, n2, n1))
elif n1 < n1:
    print('Entre {} e {}, {} é o maior.'.format(n1, n2, n2))
else:
    print('Não existe um número maior que o outro entre {} e {}'.format(n1, n2))
