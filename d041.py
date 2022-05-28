from time import sleep
from datetime import datetime
print('-=-' * 16)
print('\033[1;35;46mCATEGORIA DO ATLETA\033[m')
print('-=-' * 16)
sleep(1)
ano = int(input('Digite o ano de nascimento do atleta '))
aa = datetime.now().year
i = aa-ano
print('-=-' * 16)
print('Verificando no sistema...')
print('-=-' * 16)
sleep(1)
if i > 0 and i <= 9:
    print('O atleta tem {} anos e está na categoria \033[37mMIRIM\033[m'.format(i))
elif i > 0 and i > 9 and i <= 14:
    print('O atleta tem {} anos e está na categoria \033[33mINFANTIL\033[m'.format(i))
elif i > 0 and i > 14 and i <= 19:
    print('O atleta tem {} anos e está na categoria \033[34mJUNIOR\033[m'.format(i))
elif i > 0 and i > 19 and i <= 20:
    print('O atleta tem {} anos e está na categoria \033[35mSÊNIOR\033[m'.format(i))
elif i > 0 and i > 20:
    print('O atleta tem {} anos e está na categoria \033[31mMASTER\033[m'.format(i))
else:
    print('\033[31mOcorreu um erro. Verifique se o ano de nascimento está correto\033[m')
