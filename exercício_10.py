''' Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
- Fórmula: C = 5 * ((F-32) / 9). '''

farenheit = float(input("Insira a menida em Farenheit: "))
c = 5 * ((farenheit-32) / 9)
print("Resultado da conversão para Celsius: {}".format(c))