'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:

 Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro

 Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o
preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. '''

print("--- Tabela ---")
print("Litro gasolina: R$ 2,50")
print("Litro álcool: R$ 1,90")

tipo = (input("\nDigite a opção desejada: G - gasolina / A - álcool "))
tipo = tipo.upper()

quantLitros = float(input("Insira a quantidade de litros: "))

if (tipo == "G") and (quantLitros <= 20):
    valorSemDesconto = (quantLitros * 2.50)
    desconto = (quantLitros * 4) / 100
    valorTotal = (valorSemDesconto - desconto)
    print("Valor à pagar: R${:.2f}".format(valorTotal))

elif (tipo == "G") and (quantLitros > 20):
    valorSemDesconto = (quantLitros * 2.50)
    desconto = (quantLitros * 6) / 100
    valorTotal = (valorSemDesconto - desconto)
    print("Valor à pagar: R${:.2f}".format(valorTotal))

elif (tipo == "A") and (quantLitros <= 20):
    valorSemDesconto = (quantLitros * 1.90)
    desconto = (quantLitros * 3) / 100
    valorTotal = (valorSemDesconto - desconto)
    print("Valor à pagar: R${:.2f}".format(valorTotal))

elif (tipo == "A") and (quantLitros > 20):
    valorSemDesconto = (quantLitros * 1.90)
    desconto = (quantLitros * 5) / 100
    valorTotal = (valorSemDesconto - desconto)
    print("Valor à pagar: R${:.2f}".format(valorTotal))

print("--- Tabela ---")
print("Litro gasolina: R$ 2,50")
print("Litro álcool: R$ 1,90")

tipo = (input("\nDigite a opção desejada: G - gasolina / A - álcool "))
tipo = tipo.upper()

quantLitros = float(input("Insira a quantidade de litros: "))

if (tipo == "G") and (quantLitros <= 20):
    valorSemDesconto = (quantLitros * 2.50)
    desconto = (quantLitros * 4) / 100
    valorTotal = (valorSemDesconto - desconto)
    print("Valor à pagar: R${:.2f}".format(valorTotal))

elif (tipo == "G") and (quantLitros > 20):
    valorSemDesconto = (quantLitros * 2.50)
    desconto = (quantLitros * 6) / 100
    valorTotal = (valorSemDesconto - desconto)
    print("Valor à pagar: R${:.2f}".format(valorTotal))

elif (tipo == "A") and (quantLitros <= 20):
    valorSemDesconto = (quantLitros * 1.90)
    desconto = (quantLitros * 3) / 100
    valorTotal = (valorSemDesconto - desconto)
    print("Valor à pagar: R${:.2f}".format(valorTotal))

elif (tipo == "A") and (quantLitros > 20):
    valorSemDesconto = (quantLitros * 1.90)
    desconto = (quantLitros * 5) / 100
    valorTotal = (valorSemDesconto - desconto)
    print("Valor à pagar: R${:.2f}".format(valorTotal))