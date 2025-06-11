'''nome = input('Digite seu nome:')

print('É um prazer te conhecer,', nome,'!')'''

nome = input('Digite seu nome:')

print('É um prazer te conhecer {}{}{}'.format('\033[1;34m', nome, '\033[m'))