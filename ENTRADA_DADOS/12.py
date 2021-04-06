#Tendo como dados de entrada a altura de uma pessoa,
#construa um algoritmo que calcule seu peso ideal,
#usando a seguinte fórmula: \
#(72.7*altura) - 58

def peso(altura):
    float(altura)
    conta=(72.7*altura)-58

    return conta


if __name__ == '__main__':
    altura = float(input())
    print("PESO IDEAL {:.2f}".format(peso(altura)))