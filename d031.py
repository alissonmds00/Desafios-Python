d = int(input('Digite a distância em Km da viagem: '))
if d <= 200:
    print('O valor a ser pago é R$: {:.2f}'.format(0.5*d))
else:
    print('O valor a ser pago é R$: {:.2f}'.format(0.45*d))
