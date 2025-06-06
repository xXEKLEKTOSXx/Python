n = float(input('Digite um número: '))
km = n * 0.001
hm = n * 0.01
dam = n * 0.1
m = n * 1
dm = n * 10
cm = n * 100
mm = n * 1000

print('A medida de {}m corresponde a:\n{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(n, km, hm, dam, dm, cm, mm))