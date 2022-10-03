# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input("Digite um número aleatório: "))

if (numero > 0):
    print("O número {} é positivo.".format(numero))
elif(numero == 0):
    print("O número {} é neutro.".format(numero))
else:
    print("O número {} é negativo.".format(numero))