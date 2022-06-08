def area( ):
    print('=' * 80)
    c = int(input('Informe o valor do comprimento em metros: '))
    l = int(input('Informe o valor da largura em metros: '))
    print('-' * 80)
    a = c * l
    print(f'A área do terreno de {c}m de comprimento e {l}m de largura é igual a {a}m²')
    print('=' * 80)

area()