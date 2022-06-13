def fatorial(n=1, show='False'):
    fat = cont = n
    while cont > 1:
        cont -= 1
        fat *= cont
    if show=='False':
        return fat
    if show=='True':
        for c in range(n, 0, -1):
            if c > 1:
                print(f'{c} x ', end='')
            elif c == 1:
                print(f'{c} = {fat}')


print(fatorial(6, show='True'))