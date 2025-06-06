largura = float(input('A largura da parede é: '))
altura = float(input('A altura da parede é: '))
area = largura * altura 
qt = area / 2
print('A parede tem {} de largura, tem {} de altura, tendo assim {} m². \nA quantidade de tinta necessária, para pintar a parede, sabendo que cada litro de tinta, pinta uma área de 2m² é {} litros de tinta. '.format(largura, altura, area, qt)) 