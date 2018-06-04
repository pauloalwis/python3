numero = int(input('Digite um número para ser apresentado sua tabuada!'))

print(20 * '=')
for i in range(0, 11):
    print('{} x {:2} = {}'.format(numero, i, (numero * i)))

print(20 * '=')

