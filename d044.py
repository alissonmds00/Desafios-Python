from time import sleep
print('-=-' * 30)
print('\033[36mBem vind@ a interface de descontos!\033[m')
sleep(1.5)
print('-=-' * 30)
print('Aqui serão apresentadas algumas opções de descontos de acordo com o seu método de pagamento:')
sleep(2)
print('''1) à vista dinheiro/cheque: 10% de desconto
2) à vista no cartão: 5% de desconto
3) em até 2x no cartão: 2x sem juros
4) 3x ou mais no cartão: 20% de juros''')
print('-=-' * 30)
m = int(input('De acordo com as opções acima, selecione a opção que melhor te atende de 1 a 4: '))
v = float(input('Digite o valor total da compra: '))
if m == 1:
    print('Na compra de R$ {:.2f} no cheque/dinheiro, o valor a ser pago será de: R$ {:.2f}.'.format(v, v*0.9))
elif m == 2:
    print('Na compra da R$ {} à vista no cartão, o valor a ser pago será de R$ {:.2f}.'.format(v, v*0.95))
elif m == 3:
    print('Na compra de R$ {} parcelado em 2x no cartão, o valor a ser pago será de 2 parcelas de R$ {:.2f}'.format(v, v/2))
elif m == 4:
    p = int(input('Quantas parcelas deseja fazer? '))
    if p > 3 and p <= 24:
        print('Na compra de R$ {:.2f} parcelado de {}x, o valor a ser pago são {} parcelas de R$ {:.2f}'.format(v, p, p, (v*1.2)/p))
    else:
        print('Erro na quantidade de parcelas selecionadas')
else:
    print('\033[31mErro. Você digitou uma opção inválida.\033[m')
    print('Sua compra no valor de R$ {:.2f} vai custar R$ {:.2f}'.format(v, v))



