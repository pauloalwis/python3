# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Informe o ângulo: '))

print('O SENO do ângulo de {} é {:.2f}: '.format(angulo, sin(radians(angulo))))
print('O COSSENO do ângulo de {} é {:.2f}: '.format(angulo, cos(radians(angulo))))
print('A TANGENTE do ângulo de {} é {:.2f}: '.format(angulo, tan(radians(angulo))))
