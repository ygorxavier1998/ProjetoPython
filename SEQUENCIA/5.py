#Faça um Programa que converta metros para centímetros.

#1 metro - 100 centimetros
def conversao(metro):
    return metro*100

if __name__ == '__main__':
    Metro = float(input())
    print("metro ->{} para cm {}".format(Metro,conversao(Metro)))