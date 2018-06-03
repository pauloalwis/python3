#leia o salário de um funcionário e mostre seu novo salário com.15% de aumento
salario = float(input('Digite seu salário! '))
print('Seu salário com 15% de aumento será: {:.2f}'.format(((salario * 15) / 100) + salario))