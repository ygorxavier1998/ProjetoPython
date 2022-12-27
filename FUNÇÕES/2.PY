'''
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha. 

Faça um programa para imprimir:

        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n
'''

def canc(n):
    for item in range(n):
        for item_second in range(n):
            print(item_second+1," ",end="")
            if(item==item_second):break
        print("\n")
    
entrada = int(input("digite o numero a começar"))
canc(entrada)