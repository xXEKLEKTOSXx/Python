n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
cores = {'limpa':'\033[m', 
         'branco':'\033[0;30m', 
         'vermelho':'\033[0;31m', 
         'verde':'\033[0;32m', 
         'amarelo':'\033[0;33m', 
         'azul':'\033[0;34m', 
         'roxo':'\033[0;35m', 
         'azulclaro':'\033[0;36m', 
         'cinza':'\033[0;37m'}
print(' A primeira nota foi {}{}{}, a segunda nota foi {}{}{}, a média então é {}{:.1f}{}.'.format(cores['amarelo'], n1, cores['limpa'], cores['azul'], n2, cores['limpa'], cores['verde'], media, cores['limpa']))