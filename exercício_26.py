# Faça um programa que leia três números e mostre-os em ordem decrescente.

lista = []

for n in range(3): #Para n em alcance até 3 faça...
    n = int(input("Digite o valor: "))
    lista.append(n) #Adicionando o valor n na lista. O procedimento será realizado 3 vezes.

print()
lista.sort(reverse=True) #A função sort permite que você organize uma lista em crescente ou decrescente.
#reverse=True classifica como decrescente.
print(lista)