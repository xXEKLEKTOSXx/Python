'''n = int(input('Digite um número: '))
um = int(1)
sucessor = n + um
antecessor = n - um 
print('O número inteiro é {}, seu número sucessor é {}, e seu número antecessor é {}. '.format(n, sucessor, antecessor))'''

n = int(input('Digite um número: '))
um = int(1)
sucessor = n + um 
antecessor = n - um 
print('O número inteiro é {}{}{}, seu número sucessor é {}{}{}, e seu número antecessor é {}{}{}.'.format('\033[0;32m', n, '\033[m', '\033[0;33m', sucessor, '\033[m', '\033[0;34m', antecessor, '\033[m'))