salario = float(input('Digite um salário: '))
aumento1 = salario + (salario * 10 / 100)
aumento2 = salario + (salario * 15 / 100)
if salario > 1251:
    print('O salario de R${}\nTeve um almento de 10%, ficando no valor de R${:.2F}'.format(salario, aumento1))
else:
    print('O salario de R${}\nTeve um almento de 15%, ficando no valor de R${:.2F}'.format(salario, aumento2)) 