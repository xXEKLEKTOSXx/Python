'''vel = int(input('Escreva a velocidade do carro: '))
print('A velocidade da via é de 80Km/h, já a velocidade do carro é de {:.0f}Km/h.'.format(vel))
if vel <= 80:
    print('')
else: 
    print('Você foi multado!')'''

velocidade = float(input('Qual a velocidade do carro?'))
if velocidade > 80:
    print('Você exedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')