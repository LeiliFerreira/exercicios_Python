''' Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. '''

from time import sleep
def horario():
    turno = input("M - matutino \nV - vespertino \nN - noturno \nInforme o turno que você estuda:")
    turno = turno.upper()

    if (turno == "M"):
        print("Bom dia!")
    elif(turno == "V"):
        print("Boa tarde!")
    elif(turno == "N"):
        print("Boa noite!")

    while(turno != "M") and (turno != "V") and (turno != "N"):
        print()
        print("Valor inválido!")
        print()
        sleep(1)
        return horario()
horario()