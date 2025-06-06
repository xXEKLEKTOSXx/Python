real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar =  real / 3.27
euro = real / 6.43
iene = real / 0.03
print('Com R$ {:.2f} você pode comprar US$ {:.2f}\nVocê pode comprar €{:.2f}\nVocê pode comprar ¥{:.2f}'.format(real, dolar, euro, iene))