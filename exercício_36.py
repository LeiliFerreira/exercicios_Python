''' Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo
(resto da divisão). '''

n1 = int(input("Digite um número inteiro: "))

if (n1 % 2 == 0):
    print("O número {} é par.".format(n1))
else:
    print("O número {} é ímpar.".format(n1))