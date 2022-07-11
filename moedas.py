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


def dobro(x=0, Format=False):
    d = x*2
    return d if format is False else (moeda(d))


def moeda(v = 0, u = 'R$'):
    return f'{u} {v:.2f}'.replace('.', ',')

