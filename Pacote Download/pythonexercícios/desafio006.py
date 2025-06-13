n = int(input('Digite um número: '))
d = 2
t = 3

s1 = n * d
s2 = n * t
s3 = n ** (1/2)
print('O número é {}{}{}, vezes 2 é {}{}{}, Vezes 3 é {}{}{}, e sua raiz quadrada é {}{:.2f}{}'.format('\033[0;34m', n, '\033[m', '\033[0;33m',  s1, '\033[m', '\033[0;31m', s2, '\033[m', '\033[0;30;40m', s3, '\033[m'))