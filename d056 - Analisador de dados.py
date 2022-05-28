 from time import sleep
ci = 0
m = 0
f = 0
hmv = 0
nomemv = ''
for c in range(1, 5):
    print('-=-' * 20)
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c))).strip().capitalize()
    sexo = str(input('Qual o sexo \033[31m(M ou F)\033[m da {}ª pessoa? '.format(c))).strip().lower()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    ci = (ci+idade)
    if sexo == 'm':
        m = m + 1
        if m == 1:
            nomemv = nome
            hmv = idade
        elif m > 1 and idade > hmv:
            nomemv = nome
            hmv = idade
    elif sexo == 'f' and idade < 20:
        f += 1
print('-=-' * 20)
print('Analisando...')
sleep(2)
print('A média das idades é: {:.1f} anos'.format(ci/4))
print('{} é a pessoa do sexo masculino que é mais velha e tem {} anos.'.format(nomemv, hmv))
print('Número de mulheres abaixo dos 20 anos: {}.'.format(f))
print('-=-' * 20)

