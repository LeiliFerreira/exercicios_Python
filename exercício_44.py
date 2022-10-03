# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Crie o nome de usuário: ")
senha = input("Crie a senha: ")
nome = nome.upper()
senha = senha.upper()

quantCarac = len(senha)
crip = ("*" * quantCarac)

while(senha == nome):
    print("A senha não pode ser igual ao nome de usuário.")
    senha = input("Crie a senha: ")
    senha = senha.upper()
    if(senha != nome):
        print("\nTudo certo!")

print("\nLogin criado com sucesso!")
print("Nome de usuário: {}".format(nome))
print("Senha: {}".format(crip))