palavras = ('papel', 'borracha', 'caneta', 'mochila', 'estojo', 'lapiseira', 'apontador', 'corretivo', 'estilete', 'ak-47')
c = 1
print('-*-' * 20)
for palavra in palavras:
    if c == 1:
        print(f'Na palavra {palavra.upper()} existem as vogais: ', end='')
        c += 1
    else:
        print(f'\nNa palavra {palavra.upper()} existem as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\n'+'-*-' * 20)
















''' if 'a' or 'A' in palavras[c]:
    vogais.append('a')
if 'e' or 'E' in palavras[c]:
    vogais.append('e')
if 'i' or 'I' in palavras[c]:
    vogais.append('i')
if 'O' or 'O' in palavras[c]:
    vogais.append('o')
if 'U' or 'U' in palavras[c]:
    vogais.append('u')'''