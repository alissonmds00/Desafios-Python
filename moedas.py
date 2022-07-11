def aumentar(x=0, v=0, format=False):
    """
    Digite quantos por cento deseja aumentar
     separado por vírgula do valor
    """
    percentual = x / 100
    vf = (percentual * v) + v
    return vf if format is False else (moeda(vf))


def reduzir(x=0, v=0, format=False):
    percentual = x / 100
    vf =  v - (percentual * v)
    return vf if format is False else (moeda(vf))


def metade(x=0, format=False):
    m = x/2
    return m if format is False else (moeda(m))


def dobro(x=0, format=False):
    d = x*2
    return d if format is False else (moeda(d))


def moeda(v = 0, u = 'R$'):
    return f'{u} {v:.2f}'.replace('.', ',')


def resumo(v=0, a=0, r=0, format = False):
    if format == True:
        aum = aumentar(a, v, True)
        red = reduzir(r, v, True)
        dob = dobro(v, True)
        met = metade(v, True)
        v = moeda(v)
    else:
        aum = aumentar(a, v)
        red = reduzir(r, v)
        dob = dobro(v)
        met = metade(v)
        v = v
    print(f'{"-=-"*20}')
    print(f'{"RESUMINDO:":^60}')
    print(f'{"-=-"*20}')
    print(f'Aumentando {a}%, o resultado final é {aum}')
    print(f'Reduzindo {r}%, o resultado final é {red}')
    print(f'O dobro de {v} é {dob}')
    print(f'A metade de {v} é {met}')