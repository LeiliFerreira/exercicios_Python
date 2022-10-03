''' Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal com as seguintes
fórmulas:

- (72.7*altura) – 58 para homens
- (62.1*altura) - 44.7 para mulheres '''

altura = float(input("Digite a altura: "))
mf = int(input("Sexo: 1 - feminino / 2 - masculino\n"))

if (mf == 1):
    pesoMulher = (62.1 * altura) - 44.7
    print("O peso ideal para a sua altura é {:.2f} kg".format(pesoMulher))
elif (mf == 2):
    pesoHomem = (72.7 * altura) - 58
    print("O peso ideal para a sua altura é {:.2f} kg".format(pesoHomem))
else:
    print("Opção inválida!")