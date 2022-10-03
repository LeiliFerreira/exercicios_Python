''' Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é
sempre pelo mais barato. '''

produto1 = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))
produto3 = float(input("Digite o valor do terceiro produto: "))

if (produto1 < produto2) and (produto1 < produto3):
    print("Valor mais econômico: R${}".format(produto1))
elif(produto2 < produto1) and (produto2 < produto3):
    print("Valor mais econômico: R${}".format(produto2))
elif(produto3 < produto1) and (produto3 < produto2):
    print("Valor mais econômico: R${}".format(produto3))
elif(produto1 == produto2) and (produto2 == produto3):
    print("Todos os preços são iguais.")