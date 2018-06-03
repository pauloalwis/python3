# Leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Digite a largura de uma parede em metros! '))
altura = float(input('Digite a altura de uma parede em metros! '))

#Formula = Altura X Largura
area = largura * altura

print('Você precisa de {:.3f} litros de tintas para pintar a parede informada.'.format(area / 2))

