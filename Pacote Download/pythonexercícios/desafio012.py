preco = float(input('Qual o preço: '))
porcentagem = 5
desconto = (porcentagem / 100) * preco
vp = preco - desconto
cores = {'limpa':'\033[m', 
         'branco':'\033[0;30m', 
         'vermelho':'\033[0;31m', 
         'verde':'\033[0;32m', 
         'amarelo':'\033[0;33m', 
         'azul':'\033[0;34m', 
         'roxo':'\033[0;35m', 
         'azulclaro':'\033[0;36m', 
         'cinza':'\033[0;37m'} 
print('O valor da compra é de R${}{}{}. Por conta da promoção de 5% o valor cai para R${}{:.2f}{}.'.format( cores['verde'], preco, cores['limpa'], cores['azul'], vp, cores['limpa']))