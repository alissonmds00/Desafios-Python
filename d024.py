nome = str(input('Digite o nome da sua cidade: ')).strip()
nomec = nome.title().split()
print('O nome da sua cidade começa com Santo? \033[31m{}\033[m'.format('Santo' in nomec[0]))

'''Metodo alternativo:
nome = str(input('Digite o nome da sua cidade: ')).strip()
print(nome[:5].upper() == 'SANTO')'''
