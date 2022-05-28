nome = str(input('Digite seu nome completo ')).strip()
print(nome.lower())
print(nome.upper())
vazio = nome.replace(' ', '')
pn = nome.split()
print('O seu nome completo possui {} letras.'.format(len(vazio)))
print('O seu primeiro nome possui {} letras.'.format(len(pn[0])))

'''caminho alternativo:
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com caixa alta é {}'.format(nome.upper())
print('Seu nome com caixa baixa é {}'.format(nome.lower())
print('Seu nome completo possui {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(find(' '))'''
#Desse jeito, ele procura o primeiro espaço, que é onde o primeiro nome acaba






