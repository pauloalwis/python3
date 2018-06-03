# Alinhando a direita
print('formatando {:>20}!'.format('Alinhando'))

# Alinhando a esquerda
print('formatando {:<20}!'.format('Alinhando'))

# Alinhando ao centro
print('formatando {:^20}!'.format('Alinhando'))

# Alinhando ao centro preenchendo os espaços em branco com '='
print('formatando {:=^20}!'.format('Alinhando'))

# Alinhando a direita preenchendo os espaços a esquerda com '='
print('formatando {:=>20}!'.format('Alinhando'))

# Alinhando a esquerda preenchendo os espaços a direita com '='
print('formatando {:=<20}!'.format('Alinhando'))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaoInteiro = n1 // n2
divisaoResto = n1 % n2
potencia = n1 ** n2

print('A soma é: {}, \n '
      'A subtração é: {} \n '
      'A multiplicação é: {} \n '
      'A divisão é: {:.3f} \n '
      'A divisão inteira é: {:.3f} \n '
      'O resto da divisão é: {} \n '
      'A potência é: {} '.format(soma, subtracao, multiplicacao, divisao, divisaoInteiro, divisaoResto, potencia))
