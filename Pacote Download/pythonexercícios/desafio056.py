somaidade = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('_____ {}ª PESSOA _____'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade 
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade >        maioridadehomem: 
        maioridadehomem = idade
        nomevelho = nome 
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))