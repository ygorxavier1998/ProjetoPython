#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual 
#operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o
#número é:

#par ou ímpar;

#positivo ou negativo;

#inteiro ou decimal.


def ParImpar(x,y):
    if(x%2==0 and y%2==0):
        return print("PAR->{}\nPAR->{}".format(x,y))
    elif(x%2==0 and y%2 !=0):
        return print("PAR->{}\nIMPAR->{}".format(x,y))
    elif(x%2 != 0 and y%2 ==0):
        return print("PAR->{}\nIMPAR->{}".format(y,x))
    elif(x%2 != 0 and y%2 !=0):
        return print("IMPAR->{}\nIMPAR->{}".format(y,x))
    
    


def DecimalFloat(x,y):
    tempx = round(x)
    tempy = round(y)
    if(tempx==x and tempy==y):
        return print("AMBOS INTEIROS")
    elif(tempx==x and tempy != y):
        return print("X INTEIRO -->{}\nY DECIMAL-->{}".format(x,y))
    elif(tempx != x and tempy == y):
        return print("Y INTEIRO -->{}\nX DECIMAL-->{}".format(y,x))
    elif(tempx != x and tempy != y):
        return print("X DECIMAL -->{}\nY DECIMAL-->{}".format(x,y))



def PosiNeg(x,y):
    if(x>0 and y>0):
        return print("POSITIVO{} POSITIVO{}".format(x,y))
    elif(x>0 and y<0):
        return print("POSITIVO {} NEGATIVO {}".format(x,y))
    elif(y>0 and x<0):
        return print("POSITIVO {} NEGATIVO {}".format(y,x))
    elif(x<0 and y<0):
        return print("NEGATIVO{} NEGATIVO {}".format(y,x))




if __name__ == '__main__':

    print("digite a sua escolha\n")   
    print("PAR OU ÍMPAR--------------------1\n")
    print("POSITIVO OU NEGATIVO------------2\n")
    print("INTEIRO OU DECIMAL--------------3\n")    
    Pick = int(input())
    print("DIGITE OS NUMEROS PARA SEREM COMPUTAOD")
    numero1 = float(input())
    numero2 = float(input())

    if(Pick==1):
        print("PAR OU IMPAR")
        ParImpar(numero1,numero2)
    elif(Pick==2):
        print("POSITIVO OU NAGATIVO")
        PosiNeg(numero1,numero2)

    elif(Pick==3):
        DecimalFloat(numero1,numero2)
    else:
        print("ESCOLHA ERRADA")
