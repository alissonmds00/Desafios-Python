from random import choice
from time import sleep
print('-=-' * 20)
print('\033[1;31;46mBEM-VIND@ ao JOKEN-PO\033[m')
print('-=-' * 20)
sleep(1)
print('Vamos começar!')
print('Digite 1. para \033[31mpedra\033[m, 2. para \033[32mPapel\033[m ou 3.\033[33mTesoura.\33[m')
escolha = str(input('escolha entre Pedra, Papel e Tesoura, e tente vencer o computador! ')).strip().capitalize()
option = choice(['Pedra', 'Papel', 'Tesoura'])
print('===' * 20)
print('Sua escolha foi \033[34m{}\033[m e a do computador foi \033[35m{}\033[m'.format(escolha, option))
if option == escolha:
    print('\033[33mEMPATE\033[m! {} não vence {} e vice-versa'.format(option, escolha))
elif option == 'Pedra' and escolha == 'Papel':
    print('Você \033[32mVENCEU\033[m! Papel embrulha Pedra.')
elif option == 'Papel' and escolha == 'Pedra':
    print('Você \033[31mPERDEU\033[m. Papel embrulha Pedra.')
elif option == 'Pedra' and escolha == 'Tesoura':
    print('Você \033[31mPERDEU\033[m. Pedra destroi Tesoura.')
elif option == 'Tesoura' and escolha == 'Pedra':
    print('Você \033[32mVENCEU\033[m! Pedra destroi Tesoura.')
elif option == 'Tesoura' and escolha == 'Papel':
    print('Você \033[31mPERDEU\033[m. Tesoura corta Papel.')
elif option == 'Papel' and escolha == 'Tesoura':
    print('Você \033[32mVENCEU\033[m! Tesoura corta Papel.')
else:
    print('\033[31mERRO! Verifique se você digitou algumas das opções válidas e tente novamente.\033[m')
print('===' * 20)