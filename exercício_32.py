''' Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

        Dicas:
        Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
        Triângulo Equilátero: três lados iguais;
        Triângulo Isósceles: quaisquer dois lados iguais;
        Triângulo Escaleno: três lados diferentes; '''

lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))

teste1 = (lado1 + lado2)
teste2 = (lado2 + lado3)

if(teste1 < lado3) or (teste2 < lado1):
    print("\nNão é possível formar um triângulo!")
else:
    if(teste1 >= lado3) and (teste2 >= lado1):
        print("\nAs medidas inseridas podem formar um triângulo.")
    if (lado1 == lado2) and (lado1 == lado3) and (lado2 == lado3):
        print("\nTipo do triângulo: Equilátero.")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("\nTipo do triângulo: Isóceles.")
    elif(lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3):
        print("\nTipo do triângulo: Escaleno.")

