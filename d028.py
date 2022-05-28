import random
na = random.randint(0, 5)
print('-=-' * 20)
print('Será escolhido um número randômico pelo computador.')
print('-=-' * 20)
a = int(input('Qual o número que o computador escolheu? [0, 5]? '))

if a == na:
    print('Você acertou! O número certo é {}'.format(na))
else:
    print('Você errou. O número certo era {}'.format(na))
