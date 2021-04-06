#Faça um Programa que leia três números e mostre o maior e o menor deles.

def menor(a,b,c):
    return min(a,b,c)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(menor(a,b,c))
2