''' Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque
e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600. O programa não deve se preocupar com a quantidade
de notas existentes na máquina. '''

valorSaque = int(input("Insira o valor para saque: R$"))

if (valorSaque < 10):
    print("O valor mínimo para retirada é R$10,00")
elif (valorSaque > 600):
    print("O valor máximo para retirada é R$600,00")
else:
    cem = int(valorSaque / 100)
    valorSaque = valorSaque - (cem * 100)

    cinquenta = int(valorSaque / 50)
    valorSaque = valorSaque - (cinquenta * 50)

    dez = int(valorSaque / 10)
    valorSaque = valorSaque - (dez * 10)

    cinco = int(valorSaque / 5)
    valorSaque = valorSaque - (cinco * 5)

    um = valorSaque

    print("\nQuantidade de notas de R$100,00: {}".format(cem))
    print("Quantidade de notas de R$50,00: {}".format(cinquenta))
    print("Quantidade de notas de R$10,00: {}".format(dez))
    print("Quantidade de notas de R$5,00: {}".format(cinco))
    print("Quantidade de notas de R$1,00: {}".format(um))

valorSaque = int(input("Insira o valor para saque: R$"))

if (valorSaque < 10):
    print("O valor mínimo para retirada é R$10,00")
elif (valorSaque > 600):
    print("O valor máximo para retirada é R$600,00")
else:
    cem = int(valorSaque / 100)
    valorSaque = valorSaque - (cem * 100)

    cinquenta = int(valorSaque / 50)
    valorSaque = valorSaque - (cinquenta * 50)

    dez = int(valorSaque / 10)
    valorSaque = valorSaque - (dez * 10)

    cinco = int(valorSaque / 5)
    valorSaque = valorSaque - (cinco * 5)

    um = valorSaque

    print("\nQuantidade de notas de R$100,00: {}".format(cem))
    print("Quantidade de notas de R$50,00: {}".format(cinquenta))
    print("Quantidade de notas de R$10,00: {}".format(dez))
    print("Quantidade de notas de R$5,00: {}".format(cinco))
    print("Quantidade de notas de R$1,00: {}".format(um))