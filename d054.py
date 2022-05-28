from _datetime import datetime
aa = datetime.now().year
s = 0
i = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if aa-ano >= 21:
        s += 1
    else:
        i += 1
print('Dentre as pessoas acima, {} atingiram a maioridade e {} não.'.format(s, i))