#from math import ceil
m1 = float(input('Digite a primeira média: '))
m2 = float(input('Digite a segunda média: '))
mf = (m1+m2)/2
if mf >= 7:
    print('O aluno está \033[1;42mAPROVADO!\033[m a média do aluno é: \033[4;32m{}\033[m.'.format(mf))
elif mf < 7 and mf >= 5:
    print('O aluno deverá realizar a \033[1;46mrecuperação\033[m. sua média é: \033[4;36m{}\033[m.'.format(mf))
else:
    print('O aluno está \033[1;41mREPROVADO.\033[m a média do aluno é: \033[4;31m{}\033[m'.format(mf))
