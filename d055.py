maior = 0
menor = 0
for c in range(1, 7):
    p = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('Dentre os pesos digitados, {}kg é o maior e {}kg é o menor.'.format(maior, menor))
