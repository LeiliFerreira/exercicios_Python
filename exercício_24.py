# Faça um Programa que leia três números e mostre o MAIOR e o MENOR deles.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite outro número: "))

if (n1 > n2) and (n1 > n3):
    print("O número maior é {}.".format(n1))
elif (n2 > n1) and (n2 > n3):
    print("O número maior é {}".format(n2))
elif (n3 > n1) and (n3 > n2):
    print("O número maior é {}".format(n3))
else: 
    print("Todos os números são iguais.")

if (n1 < n2) and (n1 < n3):
    print("O número menor é {}".format(n1))
elif (n2 < n1) and (n2 < n3):
    print("O número menor é {}".format(n2))
elif (n3 < n1) and (n3 < n2):
    print("O número menor é {}".format(n3))