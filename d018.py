import math
ang = float(input('Insira o valor do ângulo desejado: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O ângulo escolhido foi {}º. O seno é igual a {:.2f}, o coseno é igual a: {:.2f}, a tangente é igual a: {:.2f}'.format(ang, sen, cos ,tg))



