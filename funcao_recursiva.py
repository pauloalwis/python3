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