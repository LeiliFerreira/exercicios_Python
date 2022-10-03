'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
        "Telefonou para a vítima?"
        "Esteve no local do crime?"
        "Mora perto da vítima?"
        "Devia para a vítima?"
        "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente". '''

print("Responda as perguntas abaixo com SIM ou NÃO:")
pergunta1 = input("Telefonou para a vítima?")
pergunta1 = pergunta1.upper()

while (pergunta1 != "SIM") and (pergunta1 != "NÃO"):
    print("\nResponda apenas com sim ou não!")
    pergunta1 = input("\nTelefonou para a vítima?")
    pergunta1 = pergunta1.upper()

pergunta2 = input("\nEsteve no local do crime?")
pergunta2 = pergunta2.upper()

while (pergunta2 != "SIM") and (pergunta2 != "NÃO"):
    print("\nResponda apenas com sim ou não!")
    pergunta2 = input("Esteve no local do crime? ")
    pergunta2 = pergunta2.upper()

pergunta3 = input("\nMora perto da vítima? ")
pergunta3 = pergunta3.upper()

while (pergunta3 != "SIM") and (pergunta3 != "NÃO"):
    print("\nResponda apenas com sim ou não!")
    pergunta3 = input("\nMora perto da vítima? ")
    pergunta3 = pergunta3.upper()

pergunta4 = input("\nDevia para a vítima?")
pergunta4 = pergunta4.upper()

while (pergunta4 != "SIM") and (pergunta4 != "NÃO"):
    print("\nResponda apenas com sim ou não!")
    pergunta4 = input("\nDevia para a vítima? ")
    pergunta4 = pergunta4.upper()

pergunta5 = input("Já trabalhou com a vítima?")
pergunta5 = pergunta5.upper()

while (pergunta5 != "SIM") and (pergunta5 != "NÃO"):
    print("\nResponda apenas com sim ou não!")
    pergunta5 = input("Já trabalhou com a vítima?")
    pergunta5 = pergunta5.upper()

situacao = 0

if (pergunta1 == "SIM"):
    situacao = (situacao + 1)
if (pergunta2 == "SIM"):
    situacao = (situacao + 1)
if (pergunta3 == "SIM"):
    situacao = (situacao + 1)
if (pergunta4 == "SIM"):
    situacao = (situacao + 1)
if (pergunta5 == "SIM"):
    situacao = (situacao + 1)

if (situacao == 2):
    print("\nConsiderado suspeito")
elif (situacao == 3) or (situacao == 4):
    print("\nConsiderado cúmplice")
elif (situacao == 5):
    print("\nConsiderado assassino")
else:
    print("\nConsiderado inocente")
