# valor de refêrencia do dolar R$ 3,27
valor = float(input('Informe um valor! '))
print('Será possível comprar {:.2f} dolares a (3,27) com o valor informado.\n '
      'Sobrando {:.2f}!'.format(valor / 3.27, valor % 3.27))
