frase = str(input('Digite a frase desejada: ')).strip()
frasec = frase.replace('A', 'a')
cores = {'vermelho':'\033[1;31m',
         'azul':'\033[1;34m',
         'bew':'\033[7m',
         'amarelo':'\033[1:33m',
         'limpa':'\033[m'}
print('A letra -A- aparece {}{}{} vezes'.format(cores['azul'], frasec.count('a'), cores['limpa']))
print('A letra -A- aparece pela primeira vez no caractere número {}{}{}'.format(cores['bew'], (frasec.find('a')+1), cores['limpa']))
print('A letra -A- aparece pela última vez no caractere número {}{}{}'.format(cores['vermelho'], (frasec.rfind('a')+1), cores['limpa']))