''' Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
- Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
- Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. '''

import math

areaPintar = float(input("Insira a área a ser pintada em m²: "))
litroMetro = 3
litrosUsar = (areaPintar / litroMetro)
litroLata = 18
quantLatas = math.ceil(litrosUsar / litroLata)

print("Quantidade de latas  de 18 litros a serem utilizadas: {}".format(quantLatas))
print("Valor unitário das latas: R$80.00")
print("Valor total: R${}".format(quantLatas*80))