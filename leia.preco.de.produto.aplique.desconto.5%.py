# Leia o preço de um produto e mostre seu novo preço, com 5% de desconto
produtoPreco = float(input('Digite o preço do produto, para aplicar o desconto de 5%.'))

print('Novo preço do produto com desconte de 5% será {:.2f}'.format(produtoPreco - ((produtoPreco * 5) / 100)))