# Um professor quer sortear um de seus quatros alunos para apagar o quadro,
# Faça um programa que ajude ele lendo o nome deles e escrevendo na tela o escolhido.

from random import choice

aluno1 = input('Informe o 1º aluno: ')
aluno2 = input('Informe o 2º aluno: ')
aluno3 = input('Informe o 3º aluno: ')
aluno4 = input('Informe o 4º aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(alunos)

print('O aluno escolhido foi {}.'.format(escolhido))
