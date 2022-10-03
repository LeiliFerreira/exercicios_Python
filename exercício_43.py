''' Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido. '''

num = float(input("Insira um número de 0 à 10: "))

while (num < 0) or (num > 10):
    num = float(input("Insira um número de 0 à 10: "))

print("O número digitado foi: {}".format(num))
