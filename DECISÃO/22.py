#Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
#Dica: utilize o operador módulo (resto da divisão).

def inteiro(x):
    return x%2

if __name__=='__main__':
    numero = int(input())
    if(inteiro(numero)==0):
        print("par")
    else:
        print("impar")