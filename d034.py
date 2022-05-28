s = float(input('Qual é o valor do seu salário em R$? '))
if s > 1250:
    print('O seu salário após o aumento será R$: {:.2f}'.format(s*1.1))
else:
    print('O seu salário após aumento será R$: {:.2f}'.format(s*1.15))
