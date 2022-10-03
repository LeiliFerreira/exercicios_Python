''' Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total
do seu salário no referido mês. '''

valorHora = float(input("Digite o valor ganho em horas: "))
horaTrabalhada = float(input("Digite a quantidade de horas trabalhadas: "))
salarioFinalMes = (valorHora * horaTrabalhada)
print("Salário mensal: R${}".format(salarioFinalMes))