a = int(input('Qual o ano que você está? '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:  # '!=' significa diferente! Pois não basta ser divisível por 4.
    print('{} é um ano bissexto.'.format(a))
else:
    print('{} não é um ano bissexto.'.format(a))
