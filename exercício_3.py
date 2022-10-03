''' Faça um programa que peça 3 números. Calcule e mostre:
- O produto do dobro do primeiro número com a metade do segundo;
- A soma do triplo do primeiro com o terceiro;
- O terceiro elevado ao cubo.'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o segundo número: "))

item1 = (num1 * 2) * (num2 / 2)
item2 = (num1 * 3) + (num3)
item3 = num3 **2

print("\n{}\n{}\n{}".format(item1, item2, item3))