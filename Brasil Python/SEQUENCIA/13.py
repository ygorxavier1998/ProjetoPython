'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcul
e seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

def peso(altura,escolha):
    if(escolha=='H' or escolha=='h'):
        float(altura)
        conta=(72.7*altura)-58
        return conta

    if (escolha == 'M' or escolha == 'm'):
        float(altura)
        conta = (62.1 * altura) - 44.7
        return conta


if __name__ == '__main__':
    altura = float(input("ALTURA:"))
    escolha = input("H/M?")
    print("PESO IDEAL {:.2f}".format(peso(altura,escolha)))