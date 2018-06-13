# Crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantos letras ao todos ( sem considerar espaços ).
# Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: "))
print("Nome com todas as letras maiúsculas: {}".format(nome.upper()))
print("Nome com todas as letras minúsculas: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras.".format(len(nome)-nome.count(' ')))

# Apresentando duas maneiras de fazer.
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))
print("Seu primeiro nome tem {} letras".format(len(nome.split()[0])))



