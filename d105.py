def boletim(*notas , sit='False'):
    resultado = {}
    if sit:
        quant = len(notas)
    else:
        quant = len(notas)
    for c in range(quant):
        if c == 0:
            resultado['maior'] = notas[c]
            resultado['menor'] = notas[c]
            resultado['média'] = notas[c]
        else:
            resultado['média'] += notas[c]
            if notas[c] > resultado['maior']:
                resultado['maior'] = notas[c]
            if notas[c] < resultado['menor']:
                resultado['menor'] = notas[c]
    resultado['média'] = (resultado['média']/quant)
    if resultado['média'] < 6:
        resultado['situação'] = 'Ruim'
    else:
        resultado['situação'] = 'Boa'
    if sit=="True":    
        return f'A maior nota é {resultado["maior"]}, A menor nota é {resultado["menor"]}, a média da turma é {resultado["média"]} e a situação é {resultado["situação"]}'
    else:
        return f'A maior nota é {resultado["maior"]}, A menor nota é {resultado["menor"]}, a média da turma é {resultado["média"]}'


média = boletim(7.5, 6.7, 8.3, 9.1, sit='True')
print(média)  
