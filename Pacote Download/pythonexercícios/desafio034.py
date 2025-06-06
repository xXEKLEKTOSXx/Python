'''salario = float(input('Digite um salário: '))
aumento1 = salario + (salario * 10 / 100)
aumento2 = salario + (salario * 15 / 100)
if salario > 1251:
    print('O salario de R${}\nTeve um almento de 10%, ficando no valor de R${:.2F}'.format(salario, aumento1))
else:
    print('O salario de R${}\nTeve um almento de 15%, ficando no valor de R${:.2F}'.format(salario, aumento2))'''

salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f} agora.'.format(salário ,novo))