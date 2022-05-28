from datetime import datetime
ano = int(input('Digite o seu ano de nascimento: '))
aa = datetime.now().year
i = aa-ano
print('você tem {} anos.'.format(aa-ano))
if i == 0:
    print('CARALHO MENOR, COMO CÊ TÁ ESCREVENDO???')
elif i == 18:
    print('Hora de capinar, família. Prepare sua enxada e a foice, e apresente-se à junta militar mais próxima.')
elif aa-ano < 18 and aa-ano != 0 and aa-ano > 0:
    print('Sua hora ainda não chegou. Faltam {} anos.'.format(abs((i-18))))
elif i > 18:
    print('Já passou da sua hora. Você está atrasado {} anos'.format(abs(i-18)))
else:
    print('Oh seu animal, você inverteu a ordem')