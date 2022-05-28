n = 0
n = int(input('Digite um número '))
c = 1
soma = n
while n != 999:
    n = int(input('Digite outro número \033[31m[999 = pausa]\033[m '))
    if n != 999:
        c += 1
        soma += n
    if n == 999:
        break
print(f'Você digitou {c} números e a soma entre eles é igual a {soma}')