# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

casas_decimais = int(input('Informe o número de decimais: '))
lado_oposto = float(input('Informe o lado oposto do triângulo/retângulo: '))
lado_adjacente = float(input('Informe o lado adjacente do triângulo/retângulo: '))

print('A Hipotenusa de um triângulo/retângulo: de 9 por 4 é {:.{}f}'.format(hypot(lado_oposto, lado_adjacente), casas_decimais))

# Maneira matemática de ser feita sem importação da classe math
hi = (lado_oposto**2 + lado_adjacente**2) ** (1/2)
print('A Hipotenusa de um triângulo/retângulo: de 9 por 4 é {:.{}f}'.format(hi, casas_decimais))