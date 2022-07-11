from Módulos import moedas
def leiaDinheiro():
    valor = str(input('Digite o valor em R$: ')).replace(',', '.')
    if valor.isnumeric():
        valor = float(valor)
    else:
        while valor.isnumeric() == False:
                valor = str(input('\033[31mValor inválido.\033[m Digite o valor em R$: ')).replace(',', '.')
    valor = float(valor)
    res = moedas.resumo(valor, 13, 20, True)



