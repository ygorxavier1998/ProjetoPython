'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 


O programa deverá pedir os valores de a, b e c e 

fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, 
a equação não é do segundo grau e o programa não deve 
fazer pedir os demais valores, sendo encerrado;

Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;

Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''
import math
def Exit():
    return 0

def Delta(A,B,C):
        D = math.pow(B,2)
        E =  4*(A*C)
        return D-E
            

def Rais(A,B,C):
    if(A==0):
       return Exit()

    if(Delta(A,B,C)==0):
        B = -1*B
        Positivo_X = ((B + 0 )/((2*A)))
        return print("positivo {}".format(Positivo_X))
        

    if(Delta(A,B,C)<0):
        return print("DELTA NNEGATIVO - SEM RAIZ POSSIVEL")
           

    if(Delta(A,B,C)>0):
        D = math.sqrt(Delta(A,B,C))
        B = -1*B
        Positivo_X = ((B + D )/((2*A)))
        print("positivo {}".format(Positivo_X))

        Negativo_X = ((B - D )/((2*A)))
        print("negativo {}".format(Negativo_X))
        
if __name__=="__main__":
    a = float(input())
    b = float(input())
    c = float(input())

    Rais(a,b,c)

