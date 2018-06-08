# Um professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

from random import shuffle

aluno1 = input('Informe o 1º aluno: ')
aluno2 = input('Informe o 2º aluno: ')
aluno3 = input('Informe o 3º aluno: ')
aluno4 = input('Informe o 4º aluno: ')

itens = [aluno1, aluno2, aluno3, aluno4]

shuffle(itens)

print('A ordem de apresentação será:')
print(itens)