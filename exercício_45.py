''' Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'. '''

nome = input("Digite o nome: ")
quantLetras = len(nome)

while(quantLetras < 3):
    print("A entrada não pode conter menos que 3 letras.")
    nome = input("Digite o nome: ")
    quantLetras = len(nome)

idade = int(input("Digite a idade: "))

while(idade < 0) or (idade > 150):
    print("Valor inválido!")
    idade = int(input("Digite a idade: "))

salario = float(input("Digite o salário: "))

while(salario < 0):
    print("Valor deve ser maior que zero.")
    salario = float(input("Digite o salário: "))

sexo = input("Digite seu sexo: 'F' ou 'M': ")
sexo = sexo.upper()

while(sexo != "F") and (sexo != "M"):
    print("Entrada inválida!")
    sexo = input("Digite seu sexo: 'F' ou 'M': ")

estadoCivil = input("Digite seu estado civil: 'S' / 'C' / 'V' / 'D': ")
estadoCivil = estadoCivil.upper()

while(estadoCivil != "S") and (estadoCivil != "C") and (estadoCivil != "V") and (estadoCivil != "V") and (estadoCivil != "D"):
    print("Entrada inválida!")
    estadoCivil = input("Digite seu estado civil: 'S' / 'C' / 'V' / 'D': ")
    estadoCivil = estadoCivil.upper()

print("\nNome..........{}".format(nome))
print("Idade..........{}".format(idade))
print("Salário..........R${:.2f}".format(salario))
print("Sexo..........{}".format(sexo))
print("Estado civil..........{}".format(estadoCivil))