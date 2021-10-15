'''Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles 
estão nos seguintes 
intervalos: 
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
'''
#A=[0-25]
#B=[26-50]
#C=[51-75]
#D=[76-100]

def main():
    A = 0
    B = 0
    C = 0
    D = 0

    while(True):
        numero = int(input())
        if(numero < 0):
            break
        if(numero <=25):
            A += 1
        if(numero >= 26 and numero <=50):
            B += 1
        if(numero >= 51 and numero <=75):
            C += 1
        if(numero >= 76 and numero <= 100):
            D += 1
    print("[0-25]={} , [26-50]={} , [51-75]={} , [76-100]={} ".format(A,B,C,D))

if __name__ == '__main__':
    main()
