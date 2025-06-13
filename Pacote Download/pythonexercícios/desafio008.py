n = float(input('Digite um número: '))
km = n * 0.001
hm = n * 0.01
dam = n * 0.1
m = n * 1
dm = n * 10
cm = n * 100
mm = n * 1000
cores = {'limpa':'\033[m', 
         'branco':'\033[0;30m', 
         'vermelho':'\033[0;31m', 
         'verde':'\033[0;32m', 
         'amarelo':'\033[0;33m', 
         'azul':'\033[0;34m', 
         'roxo':'\033[0;35m', 
         'azulclaro':'\033[0;36m', 
         'cinza':'\033[0;37m'}
print('A medida de {}m corresponde a:\n{}{:.3f}{}km\n{}{:.2f}{}hm\n{}{:.1f}{}dam\n{}{:.0f}{}dm\n{}{:.0f}{}cm\n{}{:.0f}{}mm'.format(n, cores['vermelho'], km, cores['limpa'], cores['verde'], hm, cores['limpa'], cores['amarelo'], dam, cores['limpa'], cores['azul'], dm, cores['limpa'], cores['roxo'], cm, cores['limpa'], cores['azulclaro'], mm, cores['limpa']))