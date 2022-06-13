def número(n=''):
    """
    Você precisa solicitar a função número()
    e será solicitado como parâmetro que você digite
    um número inteiro. Para solicitar o output, você deve fazer
    print(número()). Enquanto o número não for um número inteiro, o programa
    continua em loop pedindo para que adicione um valor válido. Números por extenso não serão aceitos
    Programa feito por Alisson Matias
    """
    print('-=-' * 30)
    print(f'\033[1;36m{"Validador de valores":^90}\033[m')
    num = str(input('Digite um número inteiro: ')).strip()
    if num.isnumeric():
        num = int(num)
    else:
        while num.isnumeric() == False:
            print('\033[31mErro. Digite um número inteiro válido.\033[m',end=' ')
            num = str(input('Digite um número inteiro: ')).strip()
    print('-=-' * 30)
    return num

print(f'Você digitou o número \033[35m{número()}!\033[m')