from time import sleep
print('-=-' * 16)
print('\033[1;32mSeja bem-vind@ ao programa de empréstimo!\033[m')
print('-=-' * 16)
sleep(2)
v = float(input('Qual o valor da casa que deseja comprar em R$? '))
s = float(input('Qual é a sua renda mensal em R$? '))
a = int(input('Em quantos anos deseja pagar? '))
p = v/(a*12)
print('Processando...')
sleep(2)
print('-=-' * 16)
if p > 0.3*s and s != 0:
    print('\033[1;31mOcorreu um erro.\033[m. \nO empréstimo não poderá ser aprovado, pois as parcelas excedem o valor de \033[4m30%\033[m da sua renda')
elif s == 0:
    print('\033[1;31mOcorreu um erro\033[m. \nVocê não possui a renda mínima para a contratação de um empréstimo.')
else:
    print('\033[1;32mEmpréstimo aprovado!\033[m \nAs parcelas serão no valor de \033[1;31mR$: {:.2f}\033[m por {} meses.'.format(p, a*12))

