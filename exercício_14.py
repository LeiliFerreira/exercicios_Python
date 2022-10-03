''' Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
- Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
- 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
- Salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato, e o salário líquido.
- OBS: Calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido
# OBS: Salário bruto - descontos = salário líquido. '''

ganhoHora = float(input("Insira o valor ganho por hora trabalhada: "))
totalHoras = float(input("Insira a quantidade de horas trabalhas no mês: "))
salarioBruto = (ganhoHora * totalHoras)
salarioSemDesconto = salarioBruto

#Desconto Imposto de Renda...
impostoRenda = (salarioBruto * 11) / 100
salarioBruto = (salarioBruto - impostoRenda)

#Desconto INSS...
inss = (salarioBruto * 8) / 100
salarioBruto = (salarioBruto - inss)

#Desconto Sindicato...
sindicato = (salarioBruto * 5) / 100
salarioBruto = (salarioBruto - sindicato)

salarioLiquido = salarioBruto

print("\nSalário bruto: R${:.2f}".format(salarioSemDesconto))
print("Salário líquido: R${:.2f}".format(salarioLiquido))
