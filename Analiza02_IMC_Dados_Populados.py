import numpy as np

def tabela(valIMC):
    if valIMC < 16:
        return str(valIMC) + ': Magreza grave'
    elif valIMC < 17:
        return str(valIMC) + ': Magreza moderada'
    elif valIMC < 18.5:
        return str(valIMC) + ': Magreza leve'
    elif valIMC < 25:
        return str(valIMC) + ': Saudável'
    elif valIMC < 30:
        return str(valIMC) + ': Sobrepeso'
    elif valIMC < 35:
        return str(valIMC) + ': Obesidade Grau I'
    elif valIMC < 40:
        return str(valIMC) + ': Obesidade Grau II (severe)'
    else:
        return str(valIMC) + ': Obesidade Grau III (mórbida)'


altura, peso, forca = np.loadtxt('C:/Users/paulo-note/Desktop/peso.csv',
                                 delimiter=';',
                                 unpack=True,
                                 dtype='float')

imc = peso / altura ** 2

print('Mín: ',tabela(np.amin(imc)))
print('Máx: ', tabela(np.amax(imc)))
print('Máx - Mín: ', tabela(np.ptp(imc)))
print('Média: ', tabela(np.median(imc)))
print('Média por força: ', tabela(np.average(imc)))
print('Média aritmética: ', tabela(np.mean(imc)))
print('Desvio Padrão: ', tabela(np.std(imc)))
print('Variância: ', tabela(np.var(imc)))

