''' Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
- Fórmula: medida comprimento * largura '''

comprimento = float(input("Insira o comprimento: "))
largura = float(input("Insira a largura: "))
area = (comprimento * largura)

print("Resultado da área do quadrado: {}".format(area))
print("Dobro da área: {}".format(area *2))
