from random import choice
mão = str(input('Escreva sua escolha em letras minusculas entre pedra, papel ou tesoura: '))
pedra = str()
papel = str()
tesoura = str()
lista = [pedra, papel, tesoura]
escolhido = choice(lista)
if mão == escolhido:
    print('Repita a jogada.')
