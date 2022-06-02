exp = str(input('Digite a expressão com parênteses: '))
parenteses = []
abre = 0
fecha = 0
for  v in exp:
    if v == "(" or v == ")":
        parenteses.append(v)
for c, v in enumerate(parenteses):
    if parenteses[c] == "(":
        abre += 1
    else:
        fecha += 1
if abre == fecha and parenteses[0] != ")" and parenteses[-1] != "(":
    print("A expressão é válida.")
else:
    print("A expressão não é válida.")
