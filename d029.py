from time import sleep
v = int(input('A velocidade do carro é: '))
if v > 80:
    print('\033[41mVocê foi multado em  \033[1mR$ {:.2f}\033[m'.format((v-80)*7.00))
if v == 0:
    print('\033[1;30;45mLIGA ESSE CARRO AÍ, MERMÃO!\033[m')
if v <= 80 and v != 0:
    print('\033[1;42mTudo OK.\033[m')
sleep(1.25)

print('\033[1;33mDirija com moderação!')
