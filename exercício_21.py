# Faça um programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")
letra = letra.upper()

if (letra == "A") or (letra == "E") or (letra == "I") or (letra == "O") or (letra == "U"):
    print("A letra {} é uma vogal".format(letra))
else:
    print("A letra {} é uma consoante".format(letra))
