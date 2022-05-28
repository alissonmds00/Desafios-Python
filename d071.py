from time import sleep
print('-*-' * 20)
print('Bem vindo ao simulador de caixa eletrônico ')
print('-*-' * 20)
sleep(1)
c = v = d = u = 0
i = valor = int(input('Digite o valor que deseja sacar em R$: '))
while True:
    if valor >= 50:
        c = (valor//50)
        valor = valor - (c*50)
    elif valor >= 20:
        v = (valor//20)
        valor = valor - (v*20)
    elif valor >= 10:
        d = (valor//10)
        valor = valor - (d*10)
    elif valor >= 1:
        u = (valor//1)
        valor = valor - (u*1)
    else:
        break
print(f'Convertendo R$ \033[31m{i}\033[m...')
sleep(1.2)
print(f'{c} cédulas de R$ 50,00 \n{v} cédulas de R$ 20,00 \n{d} cédulas de R$ 10,00 \n{u} cédulas de R$ 1,00')
