import math
b = int(input('Insira o valor do cateto oposto: '))
c = int(input('Insira o valor do cateto adjacente: '))
a = math.sqrt((b**2)+(c**2))
print('O valor da hipotenusa é: {:.2f}'.format(a))

