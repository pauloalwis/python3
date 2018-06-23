# Exemplo 01
# O fatorial de um número corresponde ao produto desse número
# pelo fatorial de seu número antecessor.

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

x = int(input("Digite um número para calcular seu fatorial: "))

res = factorial(x)

print("O fatorial de {} é {}".format(x ,res))

# Exemplo 02
# A sequência de Fibonacci também pode ser obtida a partir
# de uma função recursiva.

# Ela começa com os números 0 e 1, e os valores seguinte são a
# soma dos anteriores a ele, como seque:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...

