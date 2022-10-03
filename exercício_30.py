''' Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar
outro valor deve aparecer valor inválido. '''

from time import sleep
def diaSemana():
    dia = int(input("Digite um número de 1 à 7: "))
    if (dia == 1):
        print("Domingo")
    elif (dia == 2):
        print("Segunda")
    elif(dia == 3):
        print("Terça")
    elif(dia == 4):
        print("Quarta")
    elif(dia == 5):
        print("Quinta")
    elif(dia == 6):
        print("Sexta")
    elif(dia == 7):
        print("Sábado")
    else:
        print("Entrada inválida!")
        sleep(1)
        return diaSemana()
diaSemana()