'''co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O comprimento do cateto oposto é {}, o comprimento do cateto adjacente é {}, e a hipotenusa é {:.2f}'.format(co, ca, hi))'''

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('O comprimento do cateto oposto é {}, o comprimento do cateto adjacente é {}, e a hipotenusa é {:.2f}'.format(co, ca, hi))
