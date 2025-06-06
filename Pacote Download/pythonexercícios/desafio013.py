salario = float(input('Digite o salário: '))
porcentagem = 15
porcentagemaumentosalario = (salario / 100) * 15
aumentosalario = salario + porcentagemaumentosalario

print('O salário do funcionário era de R${}, mas teve um almento de 15%, indo para R${:.2f}. '.format(salario, aumentosalario))