# Programa que calcula o IMC de uma pessoa e mostra sua condição física: 

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura ** 2)

if (imc < 18.5):
    print("Abaixo do peso.")
elif(imc < 25):
    print("Saudável.")
elif(imc < 30):
    print("Peso em excesso")
elif(imc < 35):
    print("Obesidade grau 1")
elif(imc < 40):
    print("Obesidade grau 2 (severa)")
elif(imc >= 40):
    print("Obesidade grau 3 (mórbida")
