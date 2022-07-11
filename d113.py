def leiaint():
    while True:
        try:
            inteiro = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print(f'O valor digitado não é um número \033[31mINTEIRO\033[m  válido. Tente novamente: ')
            continue
        except (KeyboardInterrupt):
            print(f'O usuário preferiu não inserir um valor.')
            break
        else:
            return inteiro


def leiareal():
    while True:
        try:
            real = float(input('Digite um número real: '))
        except(ValueError, TypeError):
            print(f'O valor digitado não é um número \033[31mREAL\033[m. Digite um número real: ')
            continue
        except(KeyboardInterrupt):
            print(f'O usuário preferiu não digitar um valor. ')
            break
        else:
            return real


print(leiaint())
print(leiareal())