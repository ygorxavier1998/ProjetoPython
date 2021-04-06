#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
def maior(x):
    if(x>0):
        return True
    else:
        return False

if __name__ == '__main__':
    entrada = float(input())

    if(maior(entrada)==True):
        print("POSITIVO")
    else:
        print("NEGATIVO")