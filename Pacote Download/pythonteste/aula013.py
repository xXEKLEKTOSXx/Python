'''for c in range(0, 6):
    print('Oi')
print('Fim')'''

# Cuidado com a identação, pois da um resultado diferente.
'''for c in range(0, 6):
    print('Oi')
    print('Fim')'''

# Contagem de 1 até 5
'''for c in range(1, 7)
    print(c)
print('FIM')'''

# Contamem de 6 até 1
'''for c in range(6, 0, -1):
    print(c)
print('FIM')'''

# Contagem de 0 a 6
'''for c in range(0, 7):
    print(c)
print('FIM')'''

# Contagem de 0 a 6, pulando de 2 em 2
'''for c in range(0, 7, 2):
    print(c)
print('FIM')'''

# contagem de 0 até o número colocado
'''n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')'''

# Início, fim e passo
'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

# Comando para ler varias vezes 
'''for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')'''

# Comando para ler varias vezes, com o somatorio dos valores
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))


