n = int(input('Digite o 1º número: '))
cont = 1
soma = n
while n != 999:
    if n != 999:
        cont += 1
        n = int(input('Digite o {}º número, ou "999" para parar '.format(cont)))
        soma += n
print('Você digitou {} números e a soma entre eles é igual a {}'.format(cont, soma))