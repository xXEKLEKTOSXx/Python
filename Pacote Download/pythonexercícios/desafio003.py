'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2 

print('A soma de {} e {} é: {}'.format(n1, n2, s))'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

s = n1 + n2

print('A soma de {}{}{} e {}{}{} é: {}{}{}'.format('\033[0;31m', n1, '\033[m', '\033[0;34m', n2, '\033[m', '\033[0;35m', s, '\033[m'))