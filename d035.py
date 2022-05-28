from math import fabs
from time import sleep
print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)
sleep(1.5)
a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if fabs(b-c) < a < b + c or fabs(a-c) < b < a + c or fabs(a-b) < c < a + b:
# uma opção para a linha acima seria:
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas {}, {} e {} formam um triângulo.'.format(a, b, c))
else:
    print('As retas {}, {} e {} NÃO formam um triângulo.'.format(a, b, c))
