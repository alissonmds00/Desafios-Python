n = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão da PA? '))
c = 1
p = n
print('{} → '.format(n), end='')
while c < 10:
    c = c + 1
    p = p + r
    print('{}'.format(p), end=' → ')
print('FIM')

