al = float(input('Quantos dias alugados? '))
ro = float(input('Quantos Km rodados? '))
pagar = (60 * al) + (0.15 * ro)
print('O total a pagar é de R${:.2f}'.format(pagar))