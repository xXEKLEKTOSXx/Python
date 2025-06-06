'''import random
n = int(input('Tente adivinhar qual o número, que o PC vai escolher entre 0 e 5: '))
num = random.randint(0, 5)
print('O número entre 0 e 5, sorteado pelo PC foi {}, e o número do seu palpete foi {}.'.format(num, n))
if n == num:
    print('Você acertou, VENCEU!')
else:
    print('Você errou, PERDEU!')'''

from random import randint
from time import sleep
computador = randint(0, 5)
print('Pensei no número:{}'.format(computador)) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei?')) # O jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Vovê conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {}, e não no número {}!'.format(computador, jogador))
