d = int(input('Por quantos dias pretende alugar um carro? '))
k = float(input('Quantos km pretende rodar no total? '))
print('O valor a ser pago pelos {:.0f}km rodados durante os {:.2f} dias é: R${:.2f}'.format(k, d, (60*d)+(0.15*k)))