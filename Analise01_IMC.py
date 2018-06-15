from numpy import array

altura = [1.65, 1.70, 1.75, 1.80, 1.85]
peso = [60.0, 82.0, 82.0, 98.5, 92.8]

nAltura = array(altura)
nPeso = array(peso)

imc = nPeso / nAltura ** 2

print(imc)