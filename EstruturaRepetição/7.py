#Faça um programa que leia 5 números e informe o maior número

def Maior(a,b,c,d,e):
    return max(a,b,c,d,e)



if __name__ == '__main__':
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())  
    print("O MAIOR NUMERO: {}".format(Maior(a,b,c,d,e)))