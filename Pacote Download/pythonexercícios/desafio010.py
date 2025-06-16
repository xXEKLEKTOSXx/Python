real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar =  real / 3.27
euro = real / 6.43
iene = real / 0.03
cores = {'limpa':'\033[m', 
         'branco':'\033[0;30m', 
         'vermelho':'\033[0;31m', 
         'verde':'\033[0;32m', 
         'amarelo':'\033[0;33m', 
         'azul':'\033[0;34m', 
         'roxo':'\033[0;35m', 
         'azulclaro':'\033[0;36m', 
         'cinza':'\033[0;37m'}
print('Com R$ {}{:.2f}{} você pode comprar US$ {}{:.2f}{}\nVocê pode comprar €{}{:.2f}{}\nVocê pode comprar ¥{}{:.2f}{}'.format(cores['azul'], real, cores['limpa'], cores['verde'],dolar, cores['limpa'], cores['branco'],euro, cores['limpa'], cores['vermelho'],iene, cores['limpa']))