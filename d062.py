n = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão da PA? '))
c = 1
p = n
total = 0 #total -> pois não dá mais pra usar o 'c < 10'
mais = 10 #valor digitado pelo usuário
print('{} → '.format(n), end='')
while mais != 0:
    total = total + mais
    while c <= total:
        c = c + 1
        p = p + r
        print('{}'.format(p), end=' → ')
    print('Pausa')
    mais = int(input('Quantos mais termos da sequênciar você deseja exibir? '))
print('PA finalizada com {} termos'.format(total))



