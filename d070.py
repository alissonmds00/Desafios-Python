c = 0
t = 0
caro = 0
barato = ''
antigo = 0
while True:
    nome = str(input('Digite o nome produto ')).strip().capitalize()
    preço = float(input(f'Digite o valor de {nome} em R$ '))
    while preço < 0:
        preço = float(input(f'Digite novamente o preç ode {nome} em R$ '))
    mais = str(input('Deseja adicionar mais produtos? [S/N]: ')).strip().upper()[0]
    while mais not in 'SN':
        mais = str(input('Deseja adicionar mais produtos? [S/N]: ')).strip().upper()[0]
    c += 1
    t += preço
    if c == 1:
        barato = nome
        antigo = preço
    if c > 1:
        if preço < antigo:
            antigo = preço
            barato = nome
    if preço > 1000:
        caro += 1
    if mais == 'N':
        break
print('-*-' * 20)
print(f'Foram analisados {c} produtos')
print(f'O total da compra é R$: {t:.2f}')
print(f'Dos {c} produtos, {caro} custam mais de R$ 1000,00.')
print(f'O produto mais barato é {barato} e custa {antigo}')
print('-*-' * 20)
