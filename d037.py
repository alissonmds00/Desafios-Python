n = int(input('Digite o número inteiro que deseja converter: '))
c = int(input('Escolha a base para a qual deseja fazer a conversão \n1. para binário; \n2. para octal; \n3. para hexadecimal. \n'))
bi = bin(n)
hex = hex(n)
oct = oct(n)
if c == 1:
    print('O número \033[36m{}\033[m convertido para binário é igual a {}'.format(n, bi[2::]))
elif c == 2:
    print('O número \033[36m{}\033[m convertido para octal é igual a {}'.format(n, oct[2::]))
elif c == 3:
    print('O número \033[36m{}\033[m convertido para hexadecimal é igual a {}.'.format(n, hex[2::]))
else:
    print('\033[31mOpção invalida.\033[m')
