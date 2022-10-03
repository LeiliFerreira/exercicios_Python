''' Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
bissexto. '''

from calendar import isleap

ano = int(input("Digite o ano: "))
metodo = isleap(ano)

if (metodo == True):
    print("O ano {} é bissexto.".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))