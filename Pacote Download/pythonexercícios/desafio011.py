largura = float(input('A largura da parede é: '))
altura = float(input('A altura da parede é: '))
area = largura * altura 
qt = area / 2
cores = {'limpa':'\033[m', 
         'branco':'\033[0;30m', 
         'vermelho':'\033[0;31m', 
         'verde':'\033[0;32m', 
         'amarelo':'\033[0;33m', 
         'azul':'\033[0;34m', 
         'roxo':'\033[0;35m', 
         'azulclaro':'\033[0;36m', 
         'cinza':'\033[0;37m'}
print('A parede tem {}{}{} de largura, tem {}{}{} de altura, tendo assim {}{}{} m². \nA quantidade de tinta necessária, para pintar a parede, sabendo que cada litro de tinta, pinta uma área de 2m² é {}{}{} litros de tinta. '.format( cores['amarelo'],largura, cores['limpa'], cores['azul'],altura, cores['limpa'], cores['roxo'], area, cores['limpa'], cores['vermelho'], qt, cores['limpa'])) 