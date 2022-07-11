def aumentar(x=0, v=0):
    """
    Digite quantos por cento deseja aumentar
     separado por vírgula do valor
    """
    percentual = x / 100
    vf = (percentual * v) + v
    return vf


def reduzir(x=0, v=0):
    percentual = x / 100
    vf =  v - (percentual * v)
    return vf


def metade(x=0):
    m = x/2
    return m


def dobro(x=0):
    d = x*2
    return d


def moeda(v = 0, u = 'R$'):
    return f'{u} {v:.2f}'.replace('.', ',')

