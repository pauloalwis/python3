# valor de refêrencia do dolar R$ 3,27
valor = float(input('Quanto dinheiro você tem na carteira? R$ '))
print('Com R${:.2f} você pode comprar US${:.2f}'.format(valor, valor / 3.27))
