''' Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
- Fórmula: C/5 = (F – 32)/9 '''

c = float(input("Digite o valor em Celsius: "))
f = (c * 9 / 5) + 32
print("Resultado da conversão: {}".format(f))