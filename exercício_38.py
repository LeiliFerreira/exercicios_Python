''' Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
        par ou ímpar;
        positivo ou negativo;
        inteiro ou decimal. '''

from time import sleep

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))

print("\nOperações: ")
print("1 - somar")
print("2 - subtrair")
print("3 - multiplicar")
print("4 - dividir")
opcaoUsuario = int(input("Digite uma opção: "))

while(opcaoUsuario != 1) and (opcaoUsuario != 2) and (opcaoUsuario != 3) and (opcaoUsuario != 4):
    print("Entrada inválida!")
    sleep(1)
    opcaoUsuario = int(input("Digite uma opção: "))

if(opcaoUsuario == 1):
    soma = (n1 + n2)
    print("\nResultado da operação: {}".format(soma))

    if(soma % 2 == 0):
        print("O resultado é par")
    else:
        print("O resultado é ímpar")

    if(soma % 1 == 0):
        print("Número inteiro")
    else:
        print("Número decimal")

elif(opcaoUsuario == 2):
    subtracao = (n1 - n2)
    print("\nResultado da operação: {}".format(subtracao))

    if (subtracao % 2 == 0):
        print("O resultado é par")
    else:
        print("O resultado é ímpar")

    if (subtracao % 1 == 0):
        print("Número inteiro")
    else:
        print("Número decimal")

elif(opcaoUsuario == 3):
    multiplicacao = (n1 * n2)
    print("\nResultado da operação: {}".format(multiplicacao))

    if (multiplicacao % 2 == 0):
        print("O resultado é par")
    else:
        print("O resultado é ímpar")

    if (multiplicacao % 1 == 0):
        print("Número inteiro")
    else:
        print("Número decimal")

elif(opcaoUsuario == 4):
    divisao = (n1 / n2)
    print("\nResultado da operação: {}".format(divisao))

    if (divisao % 2 == 0):
        print("O resultado é par")
    else:
        print("O resultado é ímpar")

    if (divisao % 1 == 0):
        print("Número inteiro")
    else:
        print("Número decimal")