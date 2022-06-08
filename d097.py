def mensagem():
    msg = str(input('Informe qual mensagem você deseja que seja impressa: ')).strip()
    print('~' * len(msg) + '~' * 2)
    print(f'{" "+ msg:^}')
    print('~' * len(msg) + '~' * 2)

mensagem()