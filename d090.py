aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: ')).strip().capitalize()
aluno['media'] = float(input('Digite a média deste aluno: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else: 
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'O dado {k} nome do aluno é {v} ')

