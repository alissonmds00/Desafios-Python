f = str(input('Digite uma frase: ')).strip()
ff = f.replace(' ', '').lower()
i = ff[::-1]
if ff == i:
    print('A frase {} é um palíndromo.'.format(f))
else:
    print('A frase ´{}´ não é um palíndromo.'.format(f))
