'''Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
atual:

        salários até R$ 280,00 (incluindo) : aumento de 20%
        salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        salários de R$ 1500,00 em diante : aumento de 5%

	    Após o aumento ser realizado, informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento. '''

salarioInicial = float(input("Digite o valor do salário: R$"))

if (salarioInicial <= 280):
    reajuste = (salarioInicial * 20) / 100
    salarioReajustado = (salarioInicial + reajuste)
    print("\nSalário antes do reajuste: R${}".format(salarioInicial))
    print("Percentual do aumento aplicado: 20%")
    print("Valor do aumento: R${}".format(reajuste))
    print("Salário após aumento: R${}".format(salarioReajustado))

elif (salarioInicial > 280) and (salarioInicial < 700):
    reajuste = (salarioInicial * 15) / 100
    salarioReajustado = (salarioInicial + reajuste)
    print("\nSalário antes do reajuste: R${}".format(salarioInicial))
    print("Percentual do aumento aplicado: 15%")
    print("Valor do aumento: R${}".format(reajuste))
    print("Salário após aumento: R${}".format(salarioReajustado))

elif (salarioInicial >= 700) and (salarioInicial < 1500):
    reajuste = (salarioInicial * 10) / 100
    salarioReajustado = (salarioInicial + reajuste)
    print("\nSalário antes do reajuste: R${}".format(salarioInicial))
    print("Percentual do aumento aplicado: 10%")
    print("Valor do aumento: R${}".format(reajuste))
    print("Salário após aumento: R${}".format(salarioReajustado))

elif (salarioInicial >= 1500):
    reajuste = (salarioInicial * 5) / 100
    salarioReajustado = (salarioInicial + reajuste)
    print("\nSalário antes do reajuste: R${}".format(salarioInicial))
    print("Percentual do aumento aplicado: 5%")
    print("Valor do aumento: R${}".format(reajuste))
    print("Salário após aumento: R${}".format(salarioReajustado))