def maior(*valores):
    from time import sleep
    mai = 0
    print('-=-' * 30)
    print(f'Analisando os valores digitados... ')
    print(f'Foram digitados {len(valores)}')
    print(f'Os valores digitados são: ',end='')
    for c, v in enumerate(valores):
        if c == 0:
            mai = int(v)
        elif c > 0 and v > mai:
            mai = int(v)
        print(f'{v}', end=' ', flush=True)
        sleep(0.3)
    print()
    print(f'E o maior valor é {mai}')
    print('-=-' * 30)


maior(2, 4, 9, 1, 3, 2)
maior(1, 3, 2, 4)
maior(1, 2, 3)    
maior(8, 2, 3, 9, 4)
maior()
