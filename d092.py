from datetime import date
aa = date.today()
aa = aa.year
trabalhador = {
    'nome':str(input('Informe o nome: ')).capitalize().strip(),
    'idade':int(input('Informe a idade: ')),
}
trabalhador['ano de nascimento'] = (aa-trabalhador['idade'])
if trabalhador['idade'] >= 15:
    trabalhador['ctps'] = int(input('Informe a carteira de trabalho ou  digite [0], caso não tenha: '))
    if trabalhador['ctps'] == 0:
        trabalhador['ctps'] = 'Não tem'
    else:
            trabalhador['ano de contratação'] = int(input('Informe o  ano de contratação: '))
            trabalhador['salário R$'] = float(input('Informe o salário: '))
            trabalhador['ano de aposentadoria'] = (trabalhador['ano de contratação']+32-trabalhador['ano de nascimento'])
print('-=-' * 30)
for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}')