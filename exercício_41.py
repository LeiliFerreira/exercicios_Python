''' Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                           	Até 5 Kg           Acima de 5 Kg
        Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
        Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de
10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente. '''

print("--- Tabela de preços ---")
print("ATÉ 5 Kg: ")
print("Morango: R$ 2,50 por Kg")
print("Maçã: R$ 1,80 por kg")
print("------------------------")
print("ACIMA de 5 Kg: ")
print("Morango: R$ 2,20 por Kg")
print("Maçã: R$ 1,50 por kg")

morangos = int(input("\nDigite a quantidade de morangos kg: "))
macas = int(input("Digite a quantidade de maças kg: "))

precoMorango1 = (morangos * 2.50)
precoMorango2 = (morangos * 2.20)

precoMaca1 = (macas * 1.80)
precoMaca2 = (macas * 1.50)

if (morangos > 5):
    precoCertoMorango = precoMorango1
else:
    precoCertoMorango = precoMorango2

if (macas > 5):
    precoCertoMaca = precoMaca1
else:
    precoCertoMaca = precoMaca2

precoTotal = (precoCertoMaca + precoCertoMorango)

if (precoTotal > 25) or (macas + morangos > 8):
    precoTotal = (precoTotal * 10) / 100
    print("Valor à pagar: R${:.2f}".format(precoTotal))
else:
    print("Valor à pagar: R${:.2f}".format(precoTotal))