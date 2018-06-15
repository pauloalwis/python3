from random import uniform
from random import randint

texto = []
def obterText():
    for i in range(1, 100):
        texto.append(str(uniform(1.50, 2.20)) + ';' +
                     str(uniform(50, 120)) + ';' +
                     str(randint(0, 10)) + '\n')

def gerarArquivo():
    arq = 'C:/Users/paulo-note/Desktop/peso.csv'
    entrada = open(arq, 'w+', encoding='UTF-8')
    obterText()
    entrada.writelines(texto)
    entrada.close()

if __name__=='__main__':
    gerarArquivo()


