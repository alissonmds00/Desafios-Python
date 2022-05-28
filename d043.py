p = float(input('Digite o seu peso: '))
a = int(input('Digite a sua altura em cm: '))/100
imc = p/(a**2)
if imc < 18.5:
    print('Você tem {}kg, sua altura é {}m, seu imc é: {:.1f} e você está na categoria: abaixo do peso.'.format(p, a, imc))
elif imc >= 18.5 and imc <= 25:
    print('Você tem {}kg, sua altura é {}m, seu imc é {:.1f} e você está na categoria: peso ideal.'.format(p, a, imc))
elif imc >= 25 and imc <= 30:
    print('Você tem {}kg, sua altura é {}m, seu imc é {:.1f} e você está na categoria: sobrepeso.'.format(p, a, imc))
elif imc >= 30 and imc <= 40:
    print('Você tem {}kg, sua altura é {}m, seu imc é {:.1f} e você está na categoria: obesidade.'.format(p, a, imc))
else:
    print('Você tem {}kg, sua altura é {}m, seu imc é {:.1f} e você está na categoria: obesidade mórbida'.format(p, a, imc))
print('de acordo com o IMC, o seu peso seria ideal estando dentro de {:.1f}kg e {:.1f}kg\n'.format(18.5*(a**2), 25*(a**2)))
print('''\033[31mMas lembre-se, o importante é estar com todos os exames em dias. O IMC é impreciso e apenas algo para se basear.
Você pode estar acima do peso seugndo o IMC, mas se seus exames mostram que você está saudável, isso é o importante\033[m''')
