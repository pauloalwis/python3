# Leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Digite a largura de uma parede em metros! '))
altura = float(input('Digite a altura de uma parede em metros! '))

area = largura * altura

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você prescisará de {:.3f}l de tinta.'.format(area / 2))
