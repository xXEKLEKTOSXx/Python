'''import math
angulo = float(input("Digite um angulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo é {}, seu seno é {:.2f}, o cosseno é {:.2f}, e a tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))'''

from math import radians, sin, cos, tan 
angulo = float(input("Digite um angulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo é {}, seu seno é {:.2f}, o cosseno é {:.2f}, e a tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))