from math import fabs
a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if  fabs(b-c)<a<b+c and fabs(b-c)<b<a+c and fabs(a-b)<c<a+b:
    print('as retas de comprimento: {}, {} e {} formam um triângulo'.format(a, b, c))
    if a == b == c:
        print('e o triângulo é equilátero')
    elif a == b or a == c or b == c:
        print('e o triângulo é isósceles')
    else:
        print('e o triângulo é escaleno')
else:
    print('As retas de comprimento {}, {} e {} são incapazes de formar um triângulo.'.format(a, b, c))

