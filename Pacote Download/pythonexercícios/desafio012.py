preco = float(input('Qual o preço: '))
porcentagem = 5
desconto = (porcentagem / 100) * preco
vp = preco - desconto 
print('O valor da compra é de R${}. Por conta da promoção de 5% o valor cai para R${:.2f}.'.format(preco, vp))