def voto():
    from datetime import datetime
    anoatual = datetime.now().year
    print('-=-' * 10)
    ano = int(input('Em que ano você nasceu? '))
    print('-=-' * 10)
    global idade
    idade = anoatual - ano
    if 0 < idade < 16 :
        return f"Com {idade} anos: Não pode votar"
    elif 16 <= idade < 18 or 120 > idade > 65:
        return f"Com {idade} anos: Voto opicional"
    elif 65 > idade >= 18:
        return f"Com {idade} anos: Voto obrigatório" 
    else:
        return f"Com {idade} anos: Erro"


print(f'{voto()}')



    
