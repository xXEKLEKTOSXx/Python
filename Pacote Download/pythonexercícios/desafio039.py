from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
if nascimento == 0:
    nascimento = date.today().year
if nascimento < 18:
    print('Ainda vai se alistar ao serviço militar')
elif nascimento == 18:
    print('Hora de se alistar')
else:
    print('Passou do tempo do alistamento')
