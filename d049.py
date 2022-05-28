from time import sleep
print('==='*20)
print('''Bem vindo à tabuada 'Madeirada em Dêise'

5 -> valor que deseja exibir a tabuada 
x
10 -> valor máximo do multiplicando''')
print('==='*20)
sleep(2)
t = int(input('Digite o valor que você deseja exibir a tabuada: '))
s = int(input('Digite o valor máximo do multiplicando: '))
for c in range(1, s+1):
    print('{} x {:2} = {:2}'.format(t, c, c*t))
