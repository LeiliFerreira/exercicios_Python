''' Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
- Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
- que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

- Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor.
- Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. '''

import math

areaPintar = float(input("Informe a área a ser pintada em m²: "))

#Caso utilizando latas de 18 litros...
areaFolga = (areaPintar * 16) / 100
areaFolga = (areaPintar + areaFolga)
litroMetro = 6
litrosUsar = (areaFolga / litroMetro)
litrosLata = 18
quantLatas = math.ceil(litrosUsar / litrosLata)
print("Quantidade de latas  de 18 litros a serem utilizadas: {}".format(quantLatas))
print("Valor unitário das latas: R$80.00")
print("Valor total: R${}".format(quantLatas*80))

#Caso utilizando latas de 3.6 litros...
litrosGalao = 3.6
quantGalao = math.ceil(litrosUsar / litrosGalao)
valorApenasGalao = quantGalao * 25
print("\nQuantidade de galões de 3.6 litros a serem utilizados: {}".format(quantGalao))
print("Valor unitário: R$25.00")
print("Valor total: R${}".format(valorApenasGalao))

#Caso misturando latas e galões...
quantLatas = math.floor(litrosUsar / litrosLata)
valorLata = quantLatas * 80
litrosFaltam = litrosUsar % litrosLata
numeroGalao = math.ceil(litrosFaltam / litrosGalao)
valorGaloes = (numeroGalao * 25)

valorTotal = valorLata + valorGaloes

print("\nQuantidade de galões de 3.6 litros a serem utilizados: {}".format(numeroGalao))
print("Valor unitário: R$25.00")
print("Valor total: R${}".format(valorTotal))
