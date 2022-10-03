# Faça um programa que leia três números e mostre o maior deles.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite outro número: "))

if (n1 > n2) and (n1 > n3):
    print("O número {} é maior.".format(n1))
elif (n2 > n1) and (n2 > n3):
    print("O número {} é maior.".format(n2))
elif (n3 > n1) and (n3 > n2):
    print("O número maior é {} maior".format(n3))
else:
    print("Todos os números são iguais.")